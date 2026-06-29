from fastapi import FastAPI

from backend.schemas import EmailRequest
from backend.agents.orchestrator import AgentOrchestrator

app = FastAPI(
    title="Agentic AI Banking System",
    version="2.0"
)

orchestrator = AgentOrchestrator()


@app.get("/")
def home():

    return {
        "message": "Agentic AI Banking API Running"
    }


@app.post("/process-email")
def process_email(email: EmailRequest):

    result = orchestrator.process_email(email.model_dump())

    return result