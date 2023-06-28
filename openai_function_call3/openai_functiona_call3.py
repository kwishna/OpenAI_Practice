import json
import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_pizza_info(pizza_name: str):
    pizza_info = {
        "name": pizza_name,
        "price": "10.99",
    }
    return json.dumps(pizza_info)


def chat(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": query}],
        functions=functions,
    )
    message = response["choices"][0]["message"]
    return message


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

if __name__ == '__main__':
    # This will not use the function definition.
    print(chat("What is the capital of france?"))
    print("-" * 8)

    # This will use our function definition.
    query = "How much does pizza salami cost?"
    message = chat(query)
    print(message)
    print("-" * 8)

    if message.get("function_call"):
        # We got the function name
        function_name = message["function_call"]["name"]

        # We got the argument that needs to be passed as arguments.
        pizza_name = json.loads(message["function_call"]["arguments"]).get("pizza_name")
        print(pizza_name)
        print("-" * 8)

        # Getting the function response.
        function_response = get_pizza_info(
            pizza_name=pizza_name
        )

        # Using the function_response in the 2nd call to new response/
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": query},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        print("-" * 8)
        print(second_response)
        print(second_response.choices[0]['message']['content'])
