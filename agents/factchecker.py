from langchain_groq import ChatGroq
import os
import streamlit as st

groq_api_key = st.secrets["GROQ_API_KEY"]
tavily_api_key = st.secrets["TAVILY_API_KEY"]

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def fact_checker_agent(context):

    prompt = f"""
You are an expert fact checker.

Review the following information.

Instructions:

1. Identify verified facts.
2. Point out conflicting information.
3. Mention unsupported claims.
4. Keep verified information unchanged.

Context:

{context}
"""

    response = llm.invoke(prompt)

    return response.content
