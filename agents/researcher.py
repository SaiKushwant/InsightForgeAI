from tavily import TavilyClient
import streamlit as st

groq_api_key = st.secrets["GROQ_API_KEY"]
tavily_api_key = st.secrets["TAVILY_API_KEY"]

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def research_agent(query):
    """
    Performs web search using Tavily.
    Returns a list of search results.
    """

    response = client.search(
        query=query,
        max_results=5
    )

    return response["results"]
