# Build a Banking AI-Agent

## Objective
This project implements an agentic workflow for a banking customer support system. It processes customer requests through various nodes to determine intent, assess priority, retrieve relevant policies, draft responses, validate them, and finally route or escalate them appropriately.

## Workflow
1. **Intent Detection**: Identifies the customer intent from the input message.
2. **Priority/Risk Detection**: Classifies the issue as low, medium, or high priority.
3. **Policy Retrieval**: Retrieves relevant FAQ or policy based on the intent.
4. **Response Drafting**: Uses an LLM (Ollama) to generate a draft reply.
5. **Validation**: Validates the drafted response against policies.
6. **Routing/Escalation**: Decides to reply directly, ask for more info, or escalate to a human agent.

## Installation & Running
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Make sure Ollama is running and accessible (update `OLLAMA_BASE_URL` in `app/core/settings.py` if needed).
3. Start the application:
   ```bash
   python run.py
   ```

## Demo Video
[Insert Video URL Here]
