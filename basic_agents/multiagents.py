from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role = "search the web for information",
    model=Groq(id="Gemma2-9b-It"),
    tools = [DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True.

)

finance_agent = Agent()

