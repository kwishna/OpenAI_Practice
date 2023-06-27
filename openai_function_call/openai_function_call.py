import json
import logging
import os

import dotenv
import openai

from meta_data import calculate_metadata, getprice_meta_data
from my_secure_methods import get_price, calculate

dotenv.load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__MESSAGES = [
    {
        "role": "system",
        "content": "You're an AI assistant who is helpful to the users in conversation.",
    }
]


def openai_chat():
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613",
                                            messages=__MESSAGES,
                                            functions=[calculate_metadata, getprice_meta_data],
                                            temperature=0.7,
                                            max_tokens=50)
    return response.choices[0].message


__MESSAGES.append(
    {
        "role": "user",
        "content": "My father bought a MSFT stock at the beginning of 2000," +
                   "what is it worth now (June 2023) and what is my return?"
    }
)

while True:
    message = openai_chat()
    logger.info(message)

    __MESSAGES.append(message)

    if "function_call" not in message:
        break

    function_name = message["function_call"]["name"]
    kwargs = json.loads(message["function_call"]["arguments"])

    if function_name == "get_price":
        output = str(get_price(**kwargs))

    elif function_name == "calculate":
        output = str(calculate(**kwargs))

    else:
        raise ValueError

    __MESSAGES.append(
        {
            "role": "function",
            "name": function_name,
            "content": output
        }
    )

logger.info("------------------")
logger.info([m['role'] for m in __MESSAGES])
logger.info(__MESSAGES[-1]['content'])
logger.info("------------------")
logger.info(__MESSAGES)

# Error:-
# Rate limit reached for default-gpt-3.5-turbo in organization org-MHEuPlloB8uV1hSx4X5mpY1Q on requests per min.
# Limit: 3 / min. Please try again in 20s.
