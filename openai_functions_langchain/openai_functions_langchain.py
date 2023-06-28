import json
from typing import Optional

import openai
from dotenv import load_dotenv
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage
from langchain.tools import BaseTool
from langchain.tools import format_tool_to_openai_function, MoveFileTool

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class StupidJokeTool(BaseTool):
    name = "StupidJokeTool"
    description = "Tool to explain jokes about chickens"

    def _run(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return "It is funny, because AI..."

    async def _arun(
            self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("joke tool does not support async")


def get_pizza_info(pizza_name: str):
    pizza_info = {
        "name": pizza_name,
        "price": "10.99",
    }
    return json.dumps(pizza_info)


llm = ChatOpenAI(model="gpt-3.5-turbo-0613")

tools = [StupidJokeTool(), MoveFileTool()]
functions = [format_tool_to_openai_function(t) for t in tools]
print(functions)

query = "Why does the chicken cross the road? To get to the other side"
output = llm.predict_messages([HumanMessage(content=query)], functions=functions)
print(output)

question = json.loads(output.additional_kwargs["function_call"]["arguments"]).get("__arg1")
tool_response = tools[0].run(question)
print(tool_response)

second_response = llm.predict_messages(
    [
        HumanMessage(content=query),
        AIMessage(content=str(output.additional_kwargs)),
        ChatMessage(
            role="function",
            additional_kwargs={
                "name": output.additional_kwargs["function_call"]["name"]
            },
            content="""
                {tool_response}
            """,
        ),
    ],
    functions=functions,
)
print(second_response)
