from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="Gemma2-9b-It"),
    description="You are an assintantb please reply based on the questions",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("who won India vs england 2025 test match ?")

