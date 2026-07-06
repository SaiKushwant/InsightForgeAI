from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"

DB_PATH = BASE_DIR / "chroma_db"


embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


def ingest_pdf(pdf_path):

    loader = PyPDFLoader(str(pdf_path))

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=str(DB_PATH)
    )

    return len(chunks)