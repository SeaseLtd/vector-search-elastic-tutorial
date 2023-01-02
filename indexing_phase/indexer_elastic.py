import sys
import time
import random
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

BATCH_SIZE = 1000

# Elastic configuration.
ELASTIC_ADDRESS = "http://localhost:9200"
INDEX_NAME = "neural_index"
# Uncomment the following lines if start ES with SECURITY ENABLED.
#ELASTIC_ADDRESS = "https://localhost:9200"
#ELASTIC_PASSWORD = "<your-password>"
#CA_CERTS_PATH = "path/to/http_ca.crt"

def index_documents(documents_filename, embedding_filename, index_name, client):
    # Open the file containing text.
    with open(documents_filename, "r") as documents_file:
        # Open the file containing vectors.
        with open(embedding_filename, "r") as vectors_file:
            documents = []
            # For each document creates a JSON document including both text and related vector.
            for index, (document, vector_string) in enumerate(zip(documents_file, vectors_file)):

                vector = [float(w) for w in vector_string.split(",")]
                # Generate color value randomly (additional feature to show FILTER query behaviour).
                color = random.choice(['red', 'green', 'white', 'black'])

                doc = {
                    "_id": str(index),
                    "general_text": document,
                    "general_text_vector": vector,
                    "color": color,
                }
                # Append JSON document to a list.
                documents.append(doc)

                # To index batches of documents at a time.
                if index % BATCH_SIZE == 0 and index != 0:
                    # How you'd index data to Elastic.
                    indexing = bulk(client, documents, index=index_name)
                    documents = []
                    print("Success - %s , Failed - %s" % (indexing[0], len(indexing[1])))
            # To index the rest, when 'documents' list < BATCH_SIZE.
            if documents:
                bulk(client, documents, index=index_name)
            print("Finished")

def main():
    document_filename = sys.argv[1]
    embedding_filename = sys.argv[2]

    # Declare a client instance of the Python Elasticsearch library.
    client = Elasticsearch(hosts=[ELASTIC_ADDRESS])
    # Use this instead, IF using SECURITY ENABLED.
    # client = Elasticsearch(hosts=[ELASTIC_ADDRESS], ca_certs=CA_CERTS_PATH, basic_auth=("elastic", ELASTIC_PASSWORD))

    initial_time = time.time()
    index_documents(document_filename, embedding_filename, INDEX_NAME, client)
    finish_time = time.time()
    print('Documents indexed in {:f} seconds\n'.format(finish_time - initial_time))


if __name__ == "__main__":
    main()