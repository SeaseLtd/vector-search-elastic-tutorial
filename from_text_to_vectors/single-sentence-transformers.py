from sentence_transformers import SentenceTransformer

# The sentence we like to encode
sentences = ["what is a bank transit number"]

# Load or create a SentenceTransformer model.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# Compute sentence embeddings.
embeddings = model.encode(sentences)
# Creates a list object, comma separated.
vector = list(embeddings)
print(vector)