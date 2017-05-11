# Semantic-based closed and open domain Question Answering System (ScoQAS) Architecture [Beta]:

In the ScoQAS architecure, there are common and specific components, modules, and KBs.
This is the repository of the Ontology Based Question Answering System which process the Text questions. The ScoQA system is based on NLP techniques and presented tuple template, NSIF, and constraint. The ScoQA system performs over ontologies not over free text and operates on two scenarios, one Closed-domain, where the domain is restricted by an ontology, which using a human-made ontology and the other is Open domain where the answers are retrieved from a LOD knowledge base.

There are common and specific components, modules, and KBs. 
Some of these components are  such as  Question Preprocessing, Question Representation, Question Classifier, Building Constraints, Graph Construction, SPARQL Query Construction and Answer Extraction.

You can use these samples as a reference or as a starting point for creating your own apps. The focus here is on code structure, architecture, testing and maintainability. However, bear in mind that there are many ways to build apps with these architectures and tools, depending on your priorities, so these shouldn't be considered canonical examples.

Each components are released in their own branch. Check each componets's README for more information.
# Component samples:
- [NSIF](https://github.com/mlatifi/OntoQAS/tree/NSIF) - Building NSIF

- [Q-Preprocessing](https://github.com/mlatifi/OntoQAS/tree/Q-Preprocessing) - Question Preprocessing

- [QC](https://github.com/mlatifi/OntoQAS/tree/QC) - Question Classifier

- [Constraints](https://github.com/mlatifi/OntoQAS/tree/Constraints) - Building Constraints

- [Graph-Construction](https://github.com/mlatifi/OntoQAS/blob/Graph-Construction) - Graph Construction

This project is built by **Majid Latifi** .

# License:

- See [LICENSE](https://github.com/mlatifi/OntoQAS/tree/LICENSE)
