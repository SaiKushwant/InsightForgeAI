from pydantic import BaseModel
from typing import List,Dict


class ResearchRequest(BaseModel):
    topic: str
    model:str

class ResearchResponse(BaseModel):
    report: str
    sources: List[str]
    agent_logs: List[Dict]