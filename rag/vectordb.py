from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "data" / "resume.pdf"
DB_PATH = BASE_DIR / "chroma_db"

# Load PDF
loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Create Chroma Database
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory=str(DB_PATH)
)

print(f"Database created successfully!")
print(f"Stored {len(chunks)} chunks.")