import pandas as pd
import os
import sys
import random

EXEC_DIR = os.path.dirname(os.path.abspath(__file__))

def create_body(input_filename):
    ms_marco_corpus = pd.read_csv(input_filename, delimiter="\t", names=["general_text"])
    ms_marco_corpus['color'] = pd.Series(random.choices(['red', 'green', 'white', 'black'], k=len(ms_marco_corpus)), index=ms_marco_corpus.index)

    for index, row in ms_marco_corpus.iterrows():
        print("{\"index\": {\"_id\": \"" + str(index) + "\"}}")
        print("{\"general_text\": \"" + row['general_text'] + "\", \"color\": \"" + row['color'] + "\"}}")


def create_body_with_vectors(input_filename, input_filename_vectors):
    ms_marco_corpus = pd.read_csv(input_filename, delimiter="\t", names=["general_text"])
    ms_marco_corpus['color'] = pd.Series(random.choices(['red', 'green', 'white', 'black'], k=len(ms_marco_corpus)), index=ms_marco_corpus.index)
    ms_marco_corpus['embeddings'] = pd.read_csv(input_filename_vectors, delimiter="\t", names=["embeddings"])

    for index, row in ms_marco_corpus.iterrows():
        print("{\"index\": {\"_id\": \"" + str(index) + "\"}}")
        print("{\"general_text\": \"" + row['general_text'] + "\", \"general_text_vector\": \"" + row['embeddings'] + "\", \"color\": \"" + row['color'] + "\"}}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        input_filename = sys.argv[1]
        input_filename_vectors = sys.argv[2]
        output_filename = sys.argv[3]
        sys.stdout = open(output_filename, "w")
        create_body_with_vectors(input_filename, input_filename_vectors)
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        sys.stdout = open(output_filename, "w")
        create_body(input_filename)

    sys.stdout.close()
