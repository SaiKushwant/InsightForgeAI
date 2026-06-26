from langchain_groq import ChatGroq
import streamlit as st

groq_api_key = st.secrets["GROQ_API_KEY"]
tavily_api_key = st.secrets["TAVILY_API_KEY"]

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
