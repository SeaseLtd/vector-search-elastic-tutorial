# indexing_phase
This folder contains the material about indexing data to Elasticsearch through the Bulk API or through elasticsearch.helpers.bulk().

## Folder content:

To index batches of documents to Elasticsearch (bulk helper):

````
cd indexing_phase
python indexer_elastic.py "../from_text_to_vectors/example_input/documents_10k.tsv" "../from_text_to_vectors/example_output/vector_documents_10k.tsv"
````

To index documents to Elasticsearch using a Text Embedding Ingest Pipeline (bulk helper):

````
cd indexing_phase
python indexer_elastic_with_pipeline.py "../from_text_to_vectors/example_input/documents_10k.tsv"
````

To automatically create the body request for the Bulk API:

- with vectors

````
python create_body_for_bulk.py "../from_text_to_vectors/example_input/documents_10k.tsv" "../from_text_to_vectors/example_output/vector_documents_10k.tsv" "./example_output/documents_to_bulk.json"
````

- without vectors

````
python create_body_for_bulk.py "../from_text_to_vectors/example_input/documents_10k.tsv" "./example_output/documents_to_bulk.json"
````