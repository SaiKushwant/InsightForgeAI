def merge_context(web_results, pdf_docs):

    web_context = ""
    sources = []

    for item in web_results:

        web_context += item["content"] + "\n\n"

        sources.append(item["url"])

    pdf_context = ""

    for doc in pdf_docs:

        pdf_context += doc.page_content + "\n\n"

        if "source" in doc.metadata:
            sources.append(doc.metadata["source"])

    merged = f"""
WEB RESULTS

{web_context}

==================

DOCUMENT RESULTS

{pdf_context}
"""

    return merged, list(set(sources))