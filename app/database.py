import os

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27018")

client = AsyncIOMotorClient(MONGODB_URL)
db = client["ticket_triage"]
tickets = db["tickets"]