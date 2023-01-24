# from_text_to_vector
Text Embeddings with Elasticsearch and Open-Source Technologies

## Model:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

## Dataset:
Passage Retrieval task is recommended

https://microsoft.github.io/msmarco/Datasets.html#passage-ranking-dataset

## Folder content:
`remove_id_from_corpus.py` :  to remove the id from the MS MARCO corpus

`batch-sentence-transformers.py` :  to create vector embeddings from a corpus
- Example INPUT: documents_10k.tsv
- Example OUTPUT: vector_documents_10k.tsv

`single-sentence-transformers.py`:  to create vector embeddings from a single sentence