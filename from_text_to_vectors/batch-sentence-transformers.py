#!/usr/bin/python

from sentence_transformers import SentenceTransformer
import torch
import sys
from itertools import islice
import time

BATCH_SIZE = 100
INFO_UPDATE_FACTOR = 1

#Replace the model name to 'msmarco-distilbert-base-dot-prod-v3' to map sentences to
# a 768 dimensional dense vector space
MODEL_NAME = 'all-MiniLM-L6-v2'

# Load or create a SentenceTransformer model.
model = SentenceTransformer(MODEL_NAME)
# Get device like 'cuda'/'cpu' that should be used for computation.
if torch.cuda.is_available():
    model = model.to(torch.device("cuda"))
print(model.device)


def batch_encode_to_vectors(input_filename, output_filename):
    # Open the file containing text.
    with open(input_filename, 'r') as documents_file:
        # Open the file in which the vectors will be saved.
        with open(output_filename, 'w+') as out:
            processed = 0
            # Processing 100 documents at a time.
            for n_lines in iter(lambda: tuple(islice(documents_file, BATCH_SIZE)), ()):
                processed += 1
                if processed % INFO_UPDATE_FACTOR == 0:
                    print("Processed {} batch of documents".format(processed))
                # Create sentence embedding
                vectors = encode(n_lines)
                # Write each vector into the output file.
                for v in vectors:
                    out.write(','.join([str(i) for i in v]))
                    out.write('\n')


def encode(documents):
    embeddings = model.encode(documents, show_progress_bar=True)
    print('Vector dimension: ' + str(len(embeddings[0])))
    return embeddings

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    initial_time = time.time()
    batch_encode_to_vectors(input_filename, output_filename)
    finish_time = time.time()
    print('Vectors created in {:f} seconds\n'.format(finish_time - initial_time))

if __name__ == "__main__":
        main()
