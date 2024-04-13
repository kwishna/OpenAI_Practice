import os

from dotenv import load_dotenv

load_dotenv()

"""
API DOC - https://github.com/openai/openai-python/blob/main/api.md

"""

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant. which give response in json format."},
        {"role": "user", "content": "Give me details of most powerful chip in the world?"}
    ]
)
print(response.choices[0].message.content)
