from importlib import resources

from langgraph.graph import StateGraph, END

from state import AgentState

from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.document_search import document_search
from agents.context_merger import merge_context
from agents.factchecker import fact_checker_agent
from agents.writer import writer_agent
from agents.router import router_agent


# ---------------- Planner ----------------

def planner_node(state):
    return {
        "plan": planner_agent(state["topic"])
    }


# ---------------- Web Search ----------------

def web_search_node(state):
    return {
        "research": research_agent(state["topic"])
    }


# ---------------- PDF Search ----------------

def pdf_search_node(state):
    return {
        "pdf_context": document_search(state["topic"])
    }


# ---------------- Merge Context ----------------


def merge_node(state):

    web = state.get("research", [])

    pdf = state.get("pdf_context", [])

    merged, sources = merge_context(
        web,
        pdf
    )

    return {
        "merged_context": merged,
        "sources": sources
    }

# ---------------- Fact Checker ----------------

def factcheck_node(state):

    return {
        "verified_research":
        fact_checker_agent(
            state["merged_context"]
        )
    }
# ---------------- Writer ----------------
def writer_node(state):

    return {
        "report": writer_agent(
            state["topic"],
            state["verified_research"]
        )
    }

def router_node(state):

    return {
        "route": router_agent(state["topic"])
    }

def route_decision(state):

    route = state["route"]

    if route == "WEB":
        return "web_search"

    elif route == "PDF":
        return "pdf_search"

    else:
        return "hybrid"
    
def hybrid_node(state):

    return {
        "research": research_agent(state["topic"]),
        "pdf_context": document_search(state["topic"])
    }    

graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("web_search", web_search_node)
graph.add_node("pdf_search", pdf_search_node)
graph.add_node("merge", merge_node)
graph.add_node("factchecker", factcheck_node)
graph.add_node("writer", writer_node)
graph.add_node("router", router_node)
graph.add_node("hybrid", hybrid_node)

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "web_search": "web_search",
        "pdf_search": "pdf_search",
        "hybrid": "hybrid"
    }
)

graph.set_entry_point("planner")

graph.add_edge("planner", "router")
graph.add_edge("web_search", "merge")
graph.add_edge("pdf_search", "merge")
graph.add_edge("hybrid", "merge")

graph.add_edge("merge", "factchecker")
graph.add_edge("factchecker", "writer")
graph.add_edge("writer", END)
app_graph = graph.compile()