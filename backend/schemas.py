from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    customer_id: int = Field(..., example=100000)
    subject: str = Field(..., example="Card Charged Twice")
    body: str = Field(
        ...,
        example="My card was charged twice yesterday. Please help."
    )


class TicketResponse(BaseModel):
    ticket_id: str
    status: str
    assigned_team: str


class ConfidenceResponse(BaseModel):
    category: str
    confidence: float


class NoveltyResponse(BaseModel):
    novel: bool
    similarity: float


class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str
    tier: str
    account_type: str
    risk_score: float
    complaint_history: int
    kyc_status: str


class PolicyResponse(BaseModel):
    priority: str
    sla: str


class DecisionResponse(BaseModel):
    status: str
    team: str


class EmailProcessingResponse(BaseModel):
    ticket: TicketResponse
    confidence: ConfidenceResponse
    novelty: NoveltyResponse
    customer: CustomerResponse | None
    policy: PolicyResponse
    decision: DecisionResponse