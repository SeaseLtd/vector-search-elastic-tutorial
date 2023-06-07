from sentence_transformers import SentenceTransformer

# The sentence we like to encode
sentences = ["what is a bank transit number"]

# Load or create a SentenceTransformer model.
# Replace the model name with 'sentence-transformers/msmarco-distilbert-base-dot-prod-v3' to map the query to
# a 768 dimensional dense vector space.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Compute sentence embeddings.
embeddings = model.encode(sentences)
# Creates a list object, comma separated.
vector = list(embeddings)
print(vector)