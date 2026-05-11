import grpc
import sys
import os

# Add the root directory to sys.path so we can import the generated stubs properly
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from protos import intent_pb2, intent_pb2_grpc

from app.core.settings import settings

class IntentGrpcClient:
    def __init__(self):
        self.target = settings.INTENT_GRPC_TARGET
        # In a real production system, you might want to manage channels differently
        self.channel = grpc.insecure_channel(self.target)
        self.stub = intent_pb2_grpc.IntentServiceStub(self.channel)

    def predict_intent(self, text: str) -> str:
        try:
            request = intent_pb2.IntentRequest(text=text)
            # You can set a timeout here, e.g., timeout=10 seconds
            response = self.stub.PredictIntent(request, timeout=10)
            return response.intent
        except grpc.RpcError as e:
            print(f"gRPC Error: {e.details()} (Code: {e.code()})")
            return "default"
