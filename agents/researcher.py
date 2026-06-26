from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

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