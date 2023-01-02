# vector-search-elastic
Text Embeddings and Vector Search with Elasticsearch and Open-Source Technologies

## Pipeline:
- Produce Vectors Externally

`from_text_to_vectors`

- Index documents to Elasticsearch

`indexing_phase`

### Advance feature (Platinum or Enterprise License)

- Import and load language model to do inference directly within Elasticsearch

`nlp_models`

If you run `import_model.py` with basic license you got the following error:
````
elasticsearch.AuthorizationException: AuthorizationException(403, 'security_exception', 'current license is non-compliant for [ml]')
````
To use it, start a free trial: https://www.elastic.co/guide/en/elasticsearch/reference/current/start-trial.html

## Requirements:

To replicate this work just install the requirements.txt in your python environment.

e.g. (Python 3.8)

using pip
```
pip install -r requirements.txt
```
