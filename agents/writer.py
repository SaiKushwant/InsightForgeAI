from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def writer_agent(topic, context):

    prompt = f"""
You are an AI Research Assistant.

Topic:
{topic}

Context:
{context}

Instructions:

1. Use BOTH the Web Search results and the Uploaded Document.
2. Mention when information comes from:
   - Web Search
   - Uploaded Document
3. If both sources agree, mention that.
4. If they disagree, explain the difference.
5. Do not hallucinate information.
6. Write a professional research report.

Format:

# Executive Summary

# Key Findings

# Comparison of Sources

# Conclusion

# References
"""

    response = llm.invoke(prompt)

    return response.content

