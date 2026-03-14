from pydantic import BaseModel

class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    date: str
    time: str
    attendees: str | None = None
    topics: str
    sentiment: str
    outcome: str
    followup: str