from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime
from langchain_core.tracers import LangChainTracer

load_dotenv()

# Initialize LangChain with tracing
llm = ChatOpenAI(model="gpt-4.1", callbacks=[LangChainTracer()])

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("When was SpaceX's most recent launch? What was the missions purpose? How many days ago was that from this instant")
