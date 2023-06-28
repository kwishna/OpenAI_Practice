import json
import os

import openai
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_pizza_info(pizza_name: str):
    pizza_info = {
        "name": pizza_name,
        "price": "10.99",
    }
    return json.dumps(pizza_info)


functions = [
    {
        "name": "get_pizza_info",
        "description": "Get name and price of a pizza of the restaurant",
        "parameters": {
            "type": "object",
            "properties": {
                "pizza_name": {
                    "type": "string",
                    "description": "The name of the pizza, e.g. Salami",
                },
            },
            "required": ["pizza_name"],
        },
    }
]

llm = ChatOpenAI(model="gpt-3.5-turbo-0613")
message = llm.predict_messages(
    [HumanMessage(content="What is the capital of france?")], functions=functions
)
print("-" * 8)
print(message)
print("-" * 8)

print(message.additional_kwargs)
print("-" * 8)

query = "How much does Pizza Salami cost in the restaurant?"
message_pizza = llm.predict_messages([HumanMessage(content=query)], functions=functions)
print(message_pizza)
print("-" * 8)

print(message_pizza.additional_kwargs)
print("-" * 8)

pizza_name = json.loads(message_pizza.additional_kwargs["function_call"]["arguments"]).get("pizza_name")
print(pizza_name)
print("-" * 8)

pizza_api_response = get_pizza_info(pizza_name=pizza_name)
print(pizza_api_response)
print("-" * 8)

second_response = llm.predict_messages(
    [
        HumanMessage(content=query),
        AIMessage(content=str(message_pizza.additional_kwargs)),
        ChatMessage(
            role="function",
            additional_kwargs={
                "name": message_pizza.additional_kwargs["function_call"]["name"]
            },
            content=pizza_api_response
        ),
    ],
    functions=functions,
)
print(second_response)
print("-" * 8)
