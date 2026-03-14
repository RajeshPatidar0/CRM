from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Interaction
from database import SessionLocal, engine, Base
from schemas import InteractionCreate
from agent import run_agent

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Log interaction
@app.post("/log-interaction")
def log_interaction(data: InteractionCreate):

    db = SessionLocal()

    interaction = Interaction(**data.dict())

    db.add(interaction)
    db.commit()

    return {"message": "Interaction logged successfully"}


# Get all interactions
@app.get("/interactions")
def get_interactions():

    db = SessionLocal()

    return db.query(Interaction).all()


# AI chat
@app.post("/chat")
def chat_ai(data: dict):

    try:

        prompt = data.get("message")

        response = run_agent(prompt)

        return {"response": response}

    except Exception as e:

        return {"error": str(e)}





# uvicorn main:app --reload
