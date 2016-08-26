__author__ = 'majid'

# !/pkg/ldc/bin/python2.7
#-----------------------------------------------------------------------------
# Name:        questionProcessing.py
#
# Author:      Majid
#
# Created:     2014/06/06
# classes used by RepresentingSentences for QAS
#-----------------------------------------------------------------------------



##functions
def removeTreesFromSentences():
    global sentences, sentences2
    sentences2 =sentences
    for iS in sentences2:
        s = sentences2[iS]
        s.sint._constituents = None

def applyRuleToSentence(r,s):
    workingDirMajid=r.workingDir
    constraintOut="CONST"
    mergeOut="MERGE"
    r.removeAllIndicators()
    r.clearAllVariables()
    # r.removeFilesContent()
    if r.executeConditions(s,r):
        r.removeAllIndicators()
        r.clearAllVariables()
        r.describeBoundedOntology()
        r.executeActions(s,r)
        print "checked before currentRule,r,r.boundedVars,bv:",r,r,r.boundedVars
        if r.boundedVars:
            print "checked r.boundedVars",r.boundedVars
            obtainEAT="obtainEATs" + r.type + "(r,s,workingDirMajid)"
            exec(obtainEAT)
            obtainAnswer="obtainAnswer" + r.type + "(r,s)"
            exec(obtainAnswer)
            s.setConstraints()
            obtainConstraints="obtainConstraints" + r.type + "(r,s)"
            exec(obtainConstraints)
            buildConstraintProlog="build_Constraint_Prolog_" + r.type + "(s,workingDirMajid)"
            exec(buildConstraintProlog)
            buildConstraintGraph="build_Prolog_Graph" + "(s,workingDirMajid,constraintOut)"
            exec(buildConstraintGraph)
            # mergeGenreal_ConstraintPrologGraph(s,workingDirMajid)
            # buildMergeGraph="build_Prolog_Graph" + "(s,workingDirMajid,mergeOut)"
            # exec(buildMergeGraph)
            addEAT2Prolog_Class="addEAT2prolog_Class(r,s)"
            exec(addEAT2Prolog_Class)
          return r.type, r.id, len(r.conds), r.boundedVars, r.boundedConsts
    return None


def applyRulesToSentences():
    global sentences, databaseRules, workingDirMajid, sint
    for iR in databaseRules:
        r = databaseRules[iR]

        for iS in range(len(sentences)):
            s = sentences[iS]
            print 'applying rule', iR, 'to sentence', iS
            R=applyRuleToSentence(r,s)
            print '\n Rule Type & Rule ID  & Rule Conditions are : ', R
            print "-----------------------------------------------------------------------"

           # print sint._dependencies


def applyRulesToSentencesRange(iR,iS1,iS2):
    global sentences, databaseRules
    if iR == 'all':
        iR = databaseRules.keys()

    ok=False
    id=0
    while iS1+id<=iS2:
        # print "Rule ID: ",databaseRules[r].id, " databaseRules[r], len",databaseRules[r].type, len(lR)
        iS=int(iS1)+int(id)
        print "Sentence NO. ", id, "is :", sentences[iS]._text()
        print "Question POS list:","\n",sentences[iS].descriibe_POS()
        print "Question Named Entity (NE) list:","\n",sentences[iS].descriibe_NE()
        print "Dependencies List: ",sentences[iS].sint.describe(True)

        for r in iR:
            R = applyRuleToSentence(databaseRules[r],sentences[iS])
            if R:
                print 'Applying Rule: ', databaseRules[r].type, '--->  To Question: ', sentences[iS]._text()
                print 'Rule Success Matched!!', r, iS, R
                ok = True
                toMapSPARQLFormat(iS,sentences[iS],databaseRules[r])

        id=id+1
    print  "\n","Result of Applying Rules To Sentences : ",ok

 
def applyRulesToSentence(iR,iS):
    global sentences, databaseRules
    priorityRules=[]
    ok=False
    # print "Rule ID: ",databaseRules[r].id, " databaseRules[r], len",databaseRules[r].type, len(lR)
    print "Sentence NO. ", iS, "is :", sentences[iS]._text()
    print "Question POS list:","\n",sentences[iS].descriibe_POS()
    print "Question Named Entity (NE) list:","\n",sentences[iS].descriibe_NE()
    print "Dependencies List: ",sentences[iS].sint.describe(True)

    if iR == 'all':
        iR = databaseRules.keys()
    elif iR in databaseRules.keys():
        print "Requested Rule to run is",iR
        r=iR
        R = applyRuleToSentence(databaseRules[r],sentences[iS])

        if R:
            print 'Applying Rule: ', databaseRules[r].type, '--->  To Question: ', sentences[iS]._text()
            print 'Rule Success Matched!!', r, iS, R
            ok = True
            priorityRules.append(databaseRules[r].id)
            toMapSPARQLFormat(iS,sentences[iS],databaseRules[r])
        print "\n","Result of Applying Rules To Sentences : ",ok,priorityRules
        return ok

    else:
        print "Request Rule is not defined!!"
        return False

    for r in iR:
        R = applyRuleToSentence(databaseRules[r],sentences[iS])

        if R:
            print 'Applying Rule: ', databaseRules[r].type, '--->  To Question: ', sentences[iS]._text()
            print 'Rule Success Matched!!', r, iS, R
            ok = True
            priorityRules.append(databaseRules[r].id)
            toMapSPARQLFormat(iS,sentences[iS],databaseRules[r])
    print "\n","Result of Applying Rules To Sentences : ",ok,priorityRules



def getAllNodeCurrentGraph(r):
    global sentences
    g=Graph(r.currentGraph,r.currentGraph_Inst)
    print "New Graph was produced for rule is:","\n", g.__str__()


##main
databaseRules={}


##   Rule Type for WrPrA_1: Where    Person_tk    Action_tk       ##################

# databaseRules['WrPrA_1']=QTclassrule('WrPrA_1','Where_Person_Action')
# databaseRules['WrPrA_1'].addCondition(QTclasscondition('CWhere','isWhere(s,0)'))
# databaseRules['WrPrA_1'].addCondition(QTclasscondition('isPerson','isPerson(s)'))
# databaseRules['WrPrA_1'].addCondition(QTclasscondition('isAction','isAction(s)'))
# databaseRules['WrPrA_1'].addAction(QTclassAction('bindPerson','bindPerson(s)'))
# databaseRules['WrPrA_1'].addAction(QTclassAction('bindAction','bindAction(s)'))

##   Rule Type for WrPrA_2: Where    Person_Ontology   Action_tk       ##################

# databaseRules['WrPrA_2']=QTclassrule('WrPrA_2','Where_Person_Action')
# databaseRules['WrPrA_2'].addCondition(QTclasscondition('CWhere','isWhere(s,0)'))
# databaseRules['WrPrA_2'].addCondition(QTclasscondition('graphlook','isPersonInOntology(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_2'].addCondition(QTclasscondition('isAction','isAction(s)'))
# databaseRules['WrPrA_2'].addAction(QTclassAction('bindPersonOnt','bindPersonOnt(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_2'].addAction(QTclassAction('bindAction','bindAction(s)'))
# databaseRules['WrPrA_2'].addAction(QTclassAction('bindEAT','bindWhereOnt(s,"'+workingDirMajid+'","i_en_proper_organization")'))

##   Rule Type for WrPrA_3: Where_in    Person_Ontology   Action_tk       ##################

# databaseRules['WrPrA_3']=QTclassrule('WrPrA_3','Where_Person_Action')
# databaseRules['WrPrA_3'].addCondition(QTclasscondition('CWhere_in','isWhere_in(s)'))
# databaseRules['WrPrA_3'].addCondition(QTclasscondition('isPersonIn_Ont','isPersonIn_Ont(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_3'].addCondition(QTclasscondition('isAction','isAction(s)'))
# databaseRules['WrPrA_3'].addAction(QTclassAction('bindPersonOnt','bindPerson_Ont(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_3'].addAction(QTclassAction('bindAction','bindAction(s)'))
# databaseRules['WrPrA_3'].addAction(QTclassAction('bindWhere_in','bindWhere_in(s)'))

##   Rule Type for WrPrA_4: Where_in_Ontology    Person_Ontology   Action_tk       ##################

# databaseRules['WrPrA_4']=QTclassrule('WrPrA_4','Where_Person_Action')
# databaseRules['WrPrA_4'].addCondition(QTclasscondition('CWhere_Ont','isWhere(s,r,0)'))
# databaseRules['WrPrA_4'].addCondition(QTclasscondition('isPersonIn_Ont','isPersonIn_Ont(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_4'].addCondition(QTclasscondition('isAction','isAction(s,r)'))
# databaseRules['WrPrA_4'].addAction(QTclassAction('bindAction','bindAction(s,r)'))
# databaseRules['WrPrA_4'].addAction(QTclassAction('bindPersonOnt','bindPerson_Ont(s,"'+workingDirMajid+'","i_en_proper_person")'))
# databaseRules['WrPrA_4'].addAction(QTclassAction('bindWhere_Ont','bindWhere(s,r,0)'))


##   Rule Type for WrPrA_5: Where    Person_tk   Action_Ontology       ##################


# databaseRules['WrPrA_5']=QTclassrule('WrPrA_5','Where_Person_Action')
# databaseRules['WrPrA_5'].addCondition(QTclasscondition('CWhere','isWhere(s,0)'))
# databaseRules['WrPrA_5'].addCondition(QTclasscondition('isPerson','isPerson(s)'))
# databaseRules['WrPrA_5'].addCondition(QTclasscondition('graphlook','isActionInOntology(s,"'+workingDirMajid+'","action")'))
# databaseRules['WrPrA_5'].addAction(QTclassAction('bindPerson','bindPerson(s)'))
# databaseRules['WrPrA_5'].addAction(QTclassAction('bindAction','bindAction(s)'))
# databaseRules['WrPrA_5'].addAction(QTclassAction('bindActionOnt','bindActionOnt(s,"'+workingDirMajid+'","action")'))



#
databaseRules['WoPropPr_1']=QTclassrule('WoPropPr_1','Who_Properties_Person')
databaseRules['WoPropPr_1'].addCondition(QTclasscondition('CWho','isWho(s,r,0)'))
databaseRules['WoPropPr_1'].addCondition(QTclasscondition('isPerson','isPerson(s,r)'))
databaseRules['WoPropPr_1'].addCondition(QTclasscondition('isProperties','isProperties(s,r)'))
databaseRules['WoPropPr_1'].addAction(QTclassAction('bindPersonOnt','bindPerson_Ont(s,"'+workingDirMajid+'","i_en_proper_person")'))
databaseRules['WoPropPr_1'].addAction(QTclassAction('bindProperties','bindProperties(s,r)'))
databaseRules['WoPropPr_1'].addAction(QTclassAction('bindWho','bindWho(s,r,0)'))

workingDirMajid=databaseRules['WoPropPr_1'].workingDir
databaseRules['WoPropPr_1'].removeFilesContent()
processMajid(workingDirMajid+'depconll.conll', workingDirMajid)
from representingSentences import sentences
from representingSentences import buildSintDep
# from representingSentences import workingDirMajid

from auxiliar import SENT as mysent

print "Sentence is :", sentences[23]._text()
sentences[23].describe()


s=sentences[23]
import sys
print "Recursive stack is ",sys.getrecursionlimit()
sys.setrecursionlimit(30000)
print "Recursive stack is ",sys.getrecursionlimit()
allclasses4Sentence(s,workingDirMajid)
allslots4Sentence(s,workingDirMajid)
slots4Classes(s,workingDirMajid)
# subclasses4Class(s,workingDirMajid)
allinstances4Sentence(s,workingDirMajid)
# isPersonIn_Ont(s,workingDirMajid,"i_en_proper_person")
R=applyRuleToSentence(databaseRules['WoPropPr_1'],sentences[23])

