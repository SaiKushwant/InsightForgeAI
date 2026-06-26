# InsightForge AI – Multi-Agent Hybrid RAG Research Assistant

InsightForge AI is an intelligent multi-agent research assistant built using LangGraph that combines web search and document retrieval to generate accurate, context-aware research reports. The system employs a modular agent architecture where specialized agents collaborate to plan tasks, retrieve information, verify facts, and produce comprehensive reports.

The application integrates Tavily Search for real-time web research and ChromaDB with HuggingFace embeddings for semantic document retrieval, enabling Hybrid Retrieval-Augmented Generation (Hybrid RAG). Users can upload PDF documents, ask natural language questions through a chat-based interface, and receive detailed responses with supporting source citations.

The workflow includes a Planner Agent, Router Agent, Research Agent, Document Search Agent, Context Merger, Fact Checker, and Writer Agent orchestrated using LangGraph. An intelligent router determines whether a query requires web search, document search, or a combination of both, improving efficiency and response quality.

The frontend is developed using Streamlit, providing an intuitive interface for PDF uploads, conversational interaction, and report generation. Large language model inference is powered by Groq-hosted Llama models, delivering fast and high-quality responses suitable for research and analysis tasks.

### Key Features

* Multi-Agent AI workflow using LangGraph
* Intelligent Router Agent for dynamic workflow selection
* Hybrid RAG with web search and semantic document retrieval
* PDF upload and automatic indexing into ChromaDB
* Real-time web search using Tavily API
* Semantic search using HuggingFace Embeddings
* Fact verification and context merging
* Professional report generation with source citations
* Streamlit-based chat interface
* Groq-powered Llama models for fast inference

### Tech Stack

* Python
* LangGraph
* LangChain
* Groq API (Llama 3.3)
* Tavily Search API
* ChromaDB
* HuggingFace Embeddings
* Streamlit
* PyPDFLoader
