from fastapi import FastAPI
from app.core.schemas import ChatRequest, TraceResponse
from app.agent.orchestrator import run_workflow

app = FastAPI(title="Banking AI-Agent API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Banking AI-Agent Workflow"}

@app.post("/chat", response_model=TraceResponse)
def chat_endpoint(request: ChatRequest):
    """
    Endpoint to process a banking customer request.
    """
    trace = run_workflow(request.message)
    return trace
