from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class ChatRequest(BaseModel):
    message: str

class NodeResult(BaseModel):
    node_name: str
    output: Dict[str, Any]

class TraceResponse(BaseModel):
    request: str
    intent: Optional[str] = None
    priority: Optional[str] = None
    policy: Optional[str] = None
    draft: Optional[str] = None
    is_valid: Optional[bool] = None
    routing_decision: Optional[str] = None
    trace: List[NodeResult] = []
    final_response: Optional[str] = None
