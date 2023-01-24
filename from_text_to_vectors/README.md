# from_text_to_vector
This  folder contains all the material on Text Embeddings

## Model:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

## Dataset:
Passage Retrieval task is recommended

https://microsoft.github.io/msmarco/Datasets.html#passage-ranking-dataset

## Folder content:

To remove the id from the MS MARCO corpus:
````
python remove_id_from_corpus.py "/path/to/msmarco.tsv" "./example_input/documents_10k.tsv"
````

To create vector embeddings from the msmarco corpus:
- Example INPUT: documents_10k.tsv
- Example OUTPUT: vector_documents_10k.tsv

````
python batch-sentence-transformers.py "./example_input/documents_10k.tsv" "./example_output/vector_documents_10k.tsv"
````

To create vector embeddings from a single sentence:

````
python single-sentence-transformers.py
````