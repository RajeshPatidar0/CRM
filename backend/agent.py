
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
from dotenv import load_dotenv
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

class AgentState(TypedDict):
    message: str
    response: str


def ai_node(state):

    msg = state["message"]

    prompt = f"""
You are an AI CRM assistant for pharmaceutical sales representatives.

Analyze the interaction text and extract CRM information.

Return the response in this format:

Doctor Name:
Interaction Type:
Topics Discussed:
Sentiment (Positive/Neutral/Negative):
Outcome:
Follow-up Action:

Interaction text:
{msg}
"""

    result = llm.invoke(prompt)

    return {
        "message": msg,
        "response": result.content
    }


graph = StateGraph(AgentState)

graph.add_node("ai_node", ai_node)

graph.set_entry_point("ai_node")

graph.add_edge("ai_node", END)

app = graph.compile()


def run_agent(prompt):

    result = app.invoke({
        "message": prompt
    })

    return result["response"]

def run_agent(prompt):

    instruction = f"""
Extract CRM interaction details from the text.

Return ONLY JSON like this:

{{
 "hcp_name":"",
 "interaction_type":"Meeting",
 "topics":"",
 "sentiment":"",
 "outcome":"",
 "followup":""
}}

Interaction:
{prompt}
"""

    result = llm.invoke(instruction)

    return result.content

