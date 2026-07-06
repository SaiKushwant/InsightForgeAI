import streamlit as st
import requests
from rag.pdf_ingest import ingest_pdf
from pathlib import Path
from config import MODELS
from utils.pdf_generator import generate_pdf
from database.db import (
    save_report,
    get_reports,
    get_report,
    total_reports,
    latest_report
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="InsightForge AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ---------------- #
with st.sidebar:

    selected_model = st.selectbox(
        "🧠 Select Model",
        list(MODELS.keys())
    )

    st.title("🤖 InsightForge AI")

    ...

    st.subheader("📜 Research History")

    history = get_reports()

    for report_id, topic, created_at in history:

        if st.button(
            f"{topic[:25]}...",
            key=report_id
        ):

            previous = get_report(report_id)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": previous
                }
            )

            st.rerun()
    st.markdown("---")

    st.subheader("📊 Analytics")

    st.metric(
      "Reports Generated",
       total_reports()
)

    st.metric(

       "Last Research",
        latest_report()
)

    st.info(
        """
        **Powered By**

        • LangGraph

        • Groq (Llama 3.3)

        • Tavily

        • ChromaDB

        • HuggingFace Embeddings
        """
    )

# ---------------- Header ---------------- #

st.title("🤖 InsightForge AI")

st.caption("Hybrid Multi-Agent Research Assistant")

st.markdown(
"""
Ask any research question.

The system will automatically:

- 🌐 Search the web
- 📄 Search uploaded documents
- 🔍 Verify information
- 📝 Generate a professional report
"""
)



st.divider()
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):


        st.markdown(message["content"])    
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        save_path = UPLOAD_DIR / file.name

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        chunks = ingest_pdf(save_path)

        st.success(
            f"{file.name} indexed successfully ({chunks} chunks)"
        )
prompt = st.chat_input(
    "Ask InsightForge AI..."
       )

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    try:
       

       with st.spinner("Thinking..."):

        response = requests.post(
        "http://127.0.0.1:8000/research",
        json={
            "topic": prompt,
            "model": MODELS[selected_model]
        }
    )

        response.raise_for_status()

        result = response.json()

        report = result["report"]

        save_report(prompt, report)

        pdf_file=generate_pdf(report,f"{prompt[:20].replace(' ','_')}.pdf")

        with st.chat_message("assistant"):
            st.markdown(report)

            if "sources" in result:
                st.markdown("### 📚 Sources")

                for src in result["sources"]:
                    st.write(src)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": report
            }
        )
       with open(pdf_file, "rb") as pdf:

        st.download_button(
        "📥 Download PDF",
        data=pdf.read(),
        file_name=pdf_file,
        mime="application/pdf"
    )

    except Exception as e:

        st.error("An error occurred while generating the report.")

        st.code(str(e))

# ---------------- Footer ---------------- #

st.divider()

st.caption("InsightForge AI • Hybrid Agentic RAG Platform")