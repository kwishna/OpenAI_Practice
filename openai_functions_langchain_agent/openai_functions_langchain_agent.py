import os

import openai
from dotenv import load_dotenv
from langchain import LLMMathChain
from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]

agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

print(agent.run("What is the capital of france?"))
print(agent.run("What is 100 divided by 25?"))
