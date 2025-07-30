from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
import phi
from dotenv import load_dotenv
load_dotenv()

# Remove SSL_CERT_FILE environment variable if it exists
# This is necessary to avoid SSL errors with Groq API

if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role = "search the web for information",
    model=Groq(id="Gemma2-9b-It"),
    tools = [DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True

)

finance_agent = Agent(
    name = "Financial Agent",
    role = "Get financial data",
    model = Groq(id="Gemma2-9b-It"),
    tools = [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use table to display data",
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent (
    team=[web_agent,finance_agent],
    model=Groq(id="Gemma2-9b-It"),
    instructions=["Always include sources, Use table to display data."],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Analyze companies Tesla and Apple for which one is better to invest in?")
