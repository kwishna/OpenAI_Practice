# Q&A Prompt :-

# I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

# Q: What is human life expectancy in the United States?
# A: Human life expectancy in the United States is 78 years.

# Q: Who was president of the United States in 1955?
# A: Dwight D. Eisenhower was president of the United States in 1955.

# Q: Which party did he belong to?
# A: He belonged to the Republican Party.

# Q: What is the square root of banana?
# A: Unknown

# Q: How does a telescope work?
# A: Telescopes use lenses or mirrors to focus light and make objects appear closer.

# Q: Where were the 1992 Olympics held?
# A: The 1992 Olympics were held in Barcelona, Spain.

# Q: How many squigs are in a bonk?
# A: Unknown

# Q: Where is the Valley of Kings?
# A:

import openai

openai.api_key = "sk-"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"])

# ----------------------------------------------------------------------------------
# Grammar Correct Prompt:-

# Correct this to standard English:

# She no went to the market.

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)

# -----------------------------------------------------------------------------------
# Translates difficult text into simpler concepts. Prompt :-

# Summarize this for a second-grade student:

# Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "Summarize this for a second-grade student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
  temperature=1,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)

print(response.choices[0].message['content'])

# -----------------------------------------------------------------------------------
# Create code to call to the OpenAI API using a natural language instruction. Prompt :-

# """
# Util exposes the following:
# util.openai() -> authenticates & returns the openai module, which has the following functions:
# openai.Completion.create(
#     prompt="<my prompt>", # The prompt to start completing from
#     max_tokens=123, # The max number of tokens to generate
#     temperature=1.0 # A measure of randomness
#     echo=True, # Whether to return the prompt in addition to the generated completion
# )
# """
# import util
# """
# Create an OpenAI completion starting from the prompt "Once upon an AI", no more than 5 tokens. Does not include the prompt.
# """

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "\"\"\"\nUtil exposes the following:\nutil.openai() -> authenticates & returns the openai module, which has the following functions:\nopenai.Completion.create(\n    prompt=\"<my prompt>\", # The prompt to start completing from\n    max_tokens=123, # The max number of tokens to generate\n    temperature=1.0 # A measure of randomness\n    echo=True, # Whether to return the prompt in addition to the generated completion\n)\n\"\"\"\nimport util\n\"\"\"\nCreate an OpenAI completion starting from the prompt \"Once upon an AI\", no more than 5 tokens. Does not include the prompt.\n\"\"\"\n",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""])

print(response.choices[0].message['content'])

# -------------------------------------------------------------------------------------------
# Translate text into programmatic commands. Prompt:-

# Convert this text to a programmatic command:

# Example: Ask Constance if we need some bread
# Output: send-msg `find constance` Do we need some bread?

# Reach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "Convert this text to a programmatic command:\n\nExample: Ask Constance if we need some bread\nOutput: send-msg `find constance` Do we need some bread?\n\nReach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday",
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"])

print(response.choices[0].message['content'])

#-------------------------------------------------------------------------------------------------
# Translates English text into French, Spanish and Japanese. Prompt:-

# Translate this into 1. French, 2. Spanish and 3. Japanese:

# What rooms do you have available?

# 1.
# Sample re

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)

print(response.choices[0].message['content'])

# -------------------------------------------------------------------------------------------------------
# Translate natural language to SQL queries. Prompt :-

### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more than 10 employees in the last 3 months SELECT

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=
  "### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["#", ";"])

print(response.choices[0].message['content'])
