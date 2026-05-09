from app.nodes.intent_node import IntentNode
from app.nodes.priority_node import PriorityNode
from app.nodes.policy_node import PolicyNode
from app.nodes.draft_node import DraftNode
from app.nodes.validation_node import ValidationNode
from app.nodes.router_node import RouterNode
from app.core.schemas import TraceResponse

class AgentOrchestrator:
    def __init__(self):
        self.intent_node = IntentNode()
        self.priority_node = PriorityNode()
        self.policy_node = PolicyNode()
        self.draft_node = DraftNode()
        self.validation_node = ValidationNode()
        self.router_node = RouterNode()

    def run(self, message: str) -> TraceResponse:
        trace = []
        
        # 1. Intent Detection
        intent = self.intent_node.process(message)
        trace.append({"node_name": "IntentNode", "output": {"intent": intent}})
        
        # 2. Priority Detection
        priority = self.priority_node.process(intent, message)
        trace.append({"node_name": "PriorityNode", "output": {"priority": priority}})
        
        # 3. Policy Retrieval
        policy = self.policy_node.process(intent)
        trace.append({"node_name": "PolicyNode", "output": {"policy": policy}})
        
        # 4. Response Drafting
        draft = self.draft_node.process(message, intent, priority, policy)
        trace.append({"node_name": "DraftNode", "output": {"draft": draft}})
        
        # 5. Validation
        is_valid = self.validation_node.process(draft, policy)
        trace.append({"node_name": "ValidationNode", "output": {"is_valid": is_valid}})
        
        # 6. Routing
        routing_decision = self.router_node.process(priority, is_valid)
        trace.append({"node_name": "RouterNode", "output": {"routing_decision": routing_decision}})
        
        final_response = draft if routing_decision == "reply_directly" else "This request requires further attention or escalation."
        
        return TraceResponse(
            request=message,
            intent=intent,
            priority=priority,
            policy=policy,
            draft=draft,
            is_valid=is_valid,
            routing_decision=routing_decision,
            trace=trace,
            final_response=final_response
        )

# Global orchestrator instance
orchestrator = AgentOrchestrator()

def run_workflow(message: str) -> TraceResponse:
    return orchestrator.run(message)
