from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embedding
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

query = input("Ask a question: ")

results = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results, 1):
    print(f"Chunk {i}")
    print("-" * 60)
    print(doc.page_content)
    print()