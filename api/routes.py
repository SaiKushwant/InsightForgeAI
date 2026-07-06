from fastapi import APIRouter

from workflow import app_graph

from api.schemas import (
    ResearchRequest,
    ResearchResponse
)

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse
)
def research(request: ResearchRequest):

    result = app_graph.invoke(
    {
        "topic": request.topic,
        "model": request.model
    }
)
    print(result)
    print(result.keys())
    return ResearchResponse(

        report=result["report"],

        sources=result.get(
            "sources",
            []
        ),

        agent_logs=result.get(
            "agent_logs",
            []
        )
    )