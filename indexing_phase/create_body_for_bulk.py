import pandas as pd
import sys
import random

def create_body(input_filename):
    ms_marco_corpus = pd.read_csv(input_filename, delimiter="\t", names=["general_text"])
    ms_marco_corpus['color'] = pd.Series(random.choices(['red', 'green', 'white', 'black'], k=len(ms_marco_corpus)), index=ms_marco_corpus.index)

    for index, row in ms_marco_corpus.iterrows():
        print("{\"index\": {\"_id\": \"" + str(index) + "\"}}")
        print("{\"general_text\": \"" + row['general_text'] + "\", \"color\": \"" + row['color'] + "\"}")


def create_body_with_vectors(input_filename, input_filename_vectors_first_field, input_filename_vectors_second_field):
    ms_marco_corpus = pd.read_csv(input_filename, delimiter="\t", names=["general_text"])
    ms_marco_corpus['color'] = pd.Series(random.choices(['red', 'green', 'white', 'black'], k=len(ms_marco_corpus)), index=ms_marco_corpus.index)
    ms_marco_corpus['embeddings_384'] = pd.read_csv(input_filename_vectors_first_field, delimiter="\t", names=["embeddings_384"])
    ms_marco_corpus['embeddings_768'] = pd.read_csv(input_filename_vectors_second_field, delimiter="\t", names=["embeddings_768"])

    for index, row in ms_marco_corpus.iterrows():
        print("{\"index\": {\"_id\": \"" + str(index) + "\"}}")
        print("{\"general_text\": \"" + row['general_text'] + "\", \"general_text_vector_384\": " + "[" + row[
            'embeddings_384'] + "]" + ", \"general_text_vector_768\": " + "[" + row[
                  'embeddings_768'] + "]" + ", \"color\": \"" + row['color'] + "\"}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        input_filename = sys.argv[1]
        input_filename_vectors_384 = sys.argv[2]
        input_filename_vectors_768 = sys.argv[3]
        output_filename = sys.argv[4]
        sys.stdout = open(output_filename, "w")
        create_body_with_vectors(input_filename, input_filename_vectors_384, input_filename_vectors_768)
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        sys.stdout = open(output_filename, "w")
        create_body(input_filename)

    sys.stdout.close()
