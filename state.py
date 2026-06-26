from typing import TypedDict

class AgentState(TypedDict):
    topic: str
    plan: str
    route:str

    research: list
    pdf_context: list

    merged_context: str
    sources: list

    verified_research: str
    report: str
    
