from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = Path(__file__).resolve().parent.parent

PDF_PATH = BASE_DIR / "data" / "resume.pdf"

loader = PyPDFLoader(str(PDF_PATH))

documents = loader.load()

print(f"Pages Loaded : {len(documents)}")

print(documents[0].page_content[:500])