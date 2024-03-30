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

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Just say Ok!",
        }
    ],
    model="gpt-3.5-turbo",
)

print("===== Completion ======")
print(chat_completion)

print("===== Completion Choices Message ======")
print(chat_completion.choices[0].message.content)

# ----------------------------------------------------------------
# ----------------------- RESPONSE ----------------------------------
# ----------------------------------------------------------------

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

# ----------------------------------------------------------------
# ----------------------- STREAMING RESPONSE ----------------------------------
# ----------------------------------------------------------------

from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Just say Ok!"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

# ----------------------------------------------------------------
# ----------------------- ASYNC ---------------------
# ----------------------------------------------------------------

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test in minimum characters.",
            }
        ],
        model="gpt-3.5-turbo",
    )

# asyncio.run(main())
