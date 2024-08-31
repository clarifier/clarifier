# Clarifier (Extensible Data Cleansing Framework)

<img src="https://user-images.githubusercontent.com/6454510/178805543-800c880f-9bb9-4c14-a2e2-8db8f9f13887.png" width="100" alt="Clarifier Logo" />

Clarifier is a framework designed to provide the tools for intuitive data
quality improvement through the process of data cleansing. Built for a
thesis project at Leiden University, the software was developed to clean
data used in data science pipelines through interactive and intuitive
workflows. It should be used in the context of a consultant assisting a
user of the to-be-cleaned data with building workflows to clean data.

The framework consists of multiple core applications / services:

- Lens: React-based Workflow Editor
- Lake: Dask-wrapping DataFrame storage
- Flow: Workflow Templating & Rendering `(DAG -> BFS -> IPython)`
- Engine: GraphQL API mapping for JupyterLab Server

Clarifier features a complete REST API as well as a GraphQL API
for easily developing and integrating with other tools and systems.

Clarifier runs as multiple APIs in the [Django](https://www.djangoproject.com/)
Python framework with a [PostgreSQL](https://www.postgresql.org/) database.
