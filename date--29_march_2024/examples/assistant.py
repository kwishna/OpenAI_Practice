import time

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

'''
- Assistants can call OpenAI’s models with specific instructions to tune their personality and capabilities.
- Assistants can access multiple tools in parallel. These can be both OpenAI-hosted tools:
    — like Code interpreter and Knowledge retrieval — or tools you build / host (via Function calling).
- Assistants can access persistent Threads. Threads simplify AI application development by storing message history and truncating it
  when the conversation gets too long for the model’s context length. You create a Thread once, and simply append Messages to it as your users reply.
- Assistants can access Files in several formats — either as part of their creation or as part of Threads between Assistants and users.
  When using tools, Assistants can also create files (e.g., images, spreadsheets, etc) and cite files they reference in the Messages they create.
'''

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
)

print("checking assistant status. ")
while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "completed":
        print("done!")
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        print("messages: ")
        for message in messages:
            assert message.content[0].type == "text"
            print({"role": message.role, "message": message.content[0].text.value})

        client.beta.assistants.delete(assistant.id)

        break
    else:
        print("in progress...")
        time.sleep(5)
