from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def router_agent(query):

    prompt = f"""
You are a routing agent.

Choose ONLY one option:

WEB
PDF
HYBRID

Rules:

- Questions about uploaded documents/resume/notes/books → PDF
- Questions about latest news/trends/current events → WEB
- Questions requiring both uploaded documents and current information → HYBRID

Question:
{query}

Return ONLY:
WEB
or
PDF
or
HYBRID
"""

    response = llm.invoke(prompt)

    return response.content.strip().upper()