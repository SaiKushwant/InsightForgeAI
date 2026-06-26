from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def planner_agent(topic):

    prompt = f"""
    Break the following research topic
    into 5 research tasks.

    Topic:
    {topic}
    """

    response = llm.invoke(prompt)

    return response.content