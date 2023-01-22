import sys
import time
import random
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

BATCH_SIZE = 1000

# Elastic configuration.
ELASTIC_ADDRESS = "http://localhost:9200"
INDEX_NAME = "neural_index"
PIPELINE_NAME = "text-embeddings"

def index_documents(documents_filename, client):
    # Open the file containing text.
    with open(documents_filename, "r") as documents_file:
            documents = []
            # For each document creates a JSON document including text (and id).
            for index, document in enumerate(documents_file):
                # Generate color value randomly (additional feature to show FILTER query behaviour).
                color = random.choice(['red', 'green', 'white', 'black'])
                # Create the JSON document including index name and pipeline.
                doc = {
                    "_index": INDEX_NAME,
                    "pipeline": PIPELINE_NAME,
                    "_id": str(index),
                    "general_text": document,
                    "color": color,
                }
                # Append JSON document to a list.
                documents.append(doc)

                # To index batches of documents at a time.
                if index % BATCH_SIZE == 0 and index != 0:
                    # How you'd index data to Elastic.
                    indexing = bulk(client, documents)
                    documents = []
                    print("Success - %s , Failed - %s" % (indexing[0], len(indexing[1])))
            # To index the rest, when 'documents' list < BATCH_SIZE.
            if documents:
                bulk(client, documents)
            print("Finished")

def main():
    document_filename = sys.argv[1]

    # Declare a client instance of the Python Elasticsearch library.
    client = Elasticsearch(hosts=[ELASTIC_ADDRESS])

    initial_time = time.time()
    index_documents(document_filename, client)
    finish_time = time.time()
    print('Documents indexed in {:f} seconds\n'.format(finish_time - initial_time))


if __name__ == "__main__":
    main()