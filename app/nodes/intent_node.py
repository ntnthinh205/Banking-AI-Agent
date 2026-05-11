from app.core.settings import settings

class IntentNode:
    def __init__(self):
        print("Initializing IntentNode...")
        if settings.USE_GRPC:
            from app.clients.intent_grpc_client import IntentGrpcClient
            print(f"Using gRPC Intent Model Client (Target: {settings.INTENT_GRPC_TARGET})")
            self.grpc_client = IntentGrpcClient()
            self.model = None
        else:
            try:
                from models.intent_model.scripts.inference import IntentClassification
                print(f"Loading Local Intent Model from {settings.INTENT_MODEL_PATH}. This may take a while...")
                self.model = IntentClassification(model_path=settings.INTENT_MODEL_PATH)
            except ImportError as e:
                print(f"Warning: Could not import IntentClassification: {e}")
                self.model = None
            self.grpc_client = None

    def process(self, message: str) -> str:
        """
        Detects the intent of the message.
        """
        if settings.USE_GRPC and self.grpc_client is not None:
            return self.grpc_client.predict_intent(message)
            
        if self.model is not None:
            return self.model(message)
        
        # Fallback if both fail
        print("Model is not loaded and gRPC is disabled. Returning default.")
        return "default"
