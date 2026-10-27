from datetime import datetime, timezone

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

from app.classifier import classify_ticket
from app.database import tickets

app = FastAPI(title="Ticket Triage API")


class TicketIn(BaseModel):
    subject: str = Field(min_length=1, max_length=200)
    body: str = Field(min_length=1)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tickets", status_code=201)
async def create_ticket(ticket: TicketIn):
    result = classify_ticket(f"{ticket.subject} {ticket.body}")
    created_at = datetime.now(timezone.utc)

    inserted = await tickets.insert_one(
        {
            "subject": ticket.subject,
            "body": ticket.body,
            **result,
            "created_at": created_at,
        }
    )

    return {
        "id": str(inserted.inserted_id),
        "subject": ticket.subject,
        "body": ticket.body,
        **result,
        "created_at": created_at,
    }


@app.get("/tickets")
async def list_tickets(limit: int = Query(50, ge=1, le=100)):
    cursor = tickets.find().sort("created_at", -1).limit(limit)
    items = []
    async for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        items.append(doc)
    return items