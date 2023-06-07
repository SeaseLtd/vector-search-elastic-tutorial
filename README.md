# vector-search-elastic #
This is the repository for all the material on Text Embeddings and Vector Search with Elasticsearch and Open-Source Technologies.

For a step-by-step description read our blog posts:

[Elasticsearch Neural Search Tutorial](https://sease.io/2023/03/elasticsearch-neural-search-tutorial.html)

[Elasticsearch Neural Search Tutorial (Platinum/Enterprise)](https://sease.io/2023/03/elasticsearch-neural-search-tutorial-platinum-enterprise.html)

[Elasticsearch Neural Search Improvements in 8.6 and 8.7)](https://sease.io/2023/05/elasticsearch-neural-search-improvements-in-8-6-and-8-7.html)

## Requirements: ##

To replicate this work just install the requirements.txt in your python environment. 
e.g. (Python 3.8)

using pip
```
pip install -r requirements.txt
```

## Repository content ##
- **[from_text_to_vectors](from_text_to_vectors)**: contains the python script to generate vector embeddings from MS Marco data
  - **[example_input](from_text_to_vectors/example_input)**: contains the MS Marco data (10k)
  - **[example_output](from_text_to_vectors/example_output)**: contains the vector embeddings obtained (10k)
- **[indexing_phase](indexing_phase)**: contains the python scripts to index batches of documents to Elasticsearch at once from a file
- **[nlp_models](nlp_models)**: contains the import_model.py python script to import the all-MiniLM-L6-v2 sentence transformer from HuggingFace to Elasticsearch

## Pipeline: ##
To run Elasticsearch (after [downloading](https://www.elastic.co/downloads/past-releases#elasticsearch) it):

````
cd elasticsearch-8.8.0
bin/elasticsearch
curl localhost:9200
````

To produce vectors externally:

````
cd from_text_to_vectors
python batch-sentence-transformers.py "./example_input/documents_10k.tsv" "./example_output/vector_documents_10k_384.tsv"
````

To index batches of documents to Elasticsearch:

````
cd indexing_phase
python indexer_elastic.py "../from_text_to_vectors/example_input/documents_10k.tsv" "../from_text_to_vectors/example_output/vector_documents_10k_384.tsv" "../from_text_to_vectors/example_output/vector_documents_10k_768.tsv"
````

To transform a query into vectors:

````
cd from_text_to_vectors
python single-sentence-transformers.py
````

### Advanced feature (Platinum or Enterprise License) ###

If you run `import_model.py` with basic license you got the following error:
````
elasticsearch.AuthorizationException: AuthorizationException(403, 'security_exception', 'current license is non-compliant for [ml]')
````
To use it, start a [free trial](https://www.elastic.co/guide/en/elasticsearch/reference/current/start-trial.html):

````
curl -XPOST http://localhost:9200/_license/start_trial?acknowledge=true
````

To import and load a language model to do inference directly within Elasticsearch:

````
cd nlp_models
python import_model.py
````

To index batches of documents to Elasticsearch using a Text Embedding Ingest Pipeline:

````
cd indexing_phase
python indexer_elastic_with_pipeline.py "../from_text_to_vectors/example_input/documents_10k.tsv"
````