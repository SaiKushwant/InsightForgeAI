import streamlit as st
from workflow import app_graph
from rag.pdf_ingest import ingest_pdf
from pathlib import Path

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

    st.title("🤖 InsightForge AI")

    st.markdown("---")

    st.subheader("Pipeline")

    st.success("Planner Agent")

    st.success("Web Search (Tavily)")

    st.success("PDF Search (ChromaDB)")

    st.success("Context Merger")

    st.success("Fact Checker")

    st.success("Writer Agent")

    st.markdown("---")
    

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

            result = app_graph.invoke(
                {
                    "topic": prompt
                }
            )

        report = result["report"]

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

        st.download_button(
            "📥 Download Report",
            report,
            file_name="InsightForge_Report.md",
            mime="text/markdown"
        )

    except Exception as e:

        st.error("An error occurred while generating the report.")

        st.code(str(e))

# ---------------- Footer ---------------- #

st.divider()

st.caption("InsightForge AI • Hybrid Agentic RAG Platform")