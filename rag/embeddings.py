from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vector = embedding.embed_query("What is Retrieval Augmented Generation?")

print("Embedding Dimension:", len(vector))