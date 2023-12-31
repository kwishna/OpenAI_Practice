# OpenAI References:
import openai

openai.api_key = "sk-"

# GET - https://api.openai.com/v1/models - List all the models
# print(len(openai.Model.list()))

# GET - https://api.openai.com/v1/models/{model} - Retrieves a model instance, providing basic information about the model such as the owner and permissioning.
# print(openai.Model.retrieve("text-davinci-003"))

# NodeJS |
# ---------------------------------------------------
# import { Configuration, OpenAIApi } from "openai";
# const configuration = new Configuration({
#     organization: "YOUR_ORG_ID",
#     apiKey: process.env.OPENAI_API_KEY,
# });
# const openai = new OpenAIApi(configuration);
# const response = await openai.listEngines();
# ---------------------------------------------------

# POST https://api.openai.com/v1/chat/completions - Creates a model response for the given chat conversation.


def chat(prompt):
  messages = [{
    "role":
    "system",
    "content":
    "You're an helpful AI assistant that assists the users based on research papers, magazines & expert's articles. Reply in the minimal words."
  }, {
    "role": "user",
    "content": prompt
  }]

  # https://api.openai.com/v1/chat/completions
  # Headers - Authorization: Bearer $OPENAI_API_KEY
  response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                          messages=messages,
                                          temperature=0.7,
                                          max_tokens=20)
  return response.choices[0].message['content']
  # We can see the 'finish_reason' is 'stop' which means the API returned the full completion generated by the model.


# print(chat("Hello, AI."))

# -------------------------------------------------------------------------------
# Create Completion
# POST https://api.openai.com/v1/completions


def query(prompt: str):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=prompt,
                                      max_tokens=20,
                                      temperature=0)
  return response.choices[0].text


# print(query("Where is the capital of France?"))

# ---------------------------------------------------------------------------------
# Create edit
# POST https://api.openai.com/v1/edits - Creates a new edit for the provided input, instruction, and parameters.


def edit(sentence, instruction):
  response = openai.Edit.create(model="text-davinci-edit-001",
                                input=sentence,
                                instruction=instruction)

  return response.choices[0].text


# print(edit("What day of the wek is it?", "Fix the spelling mistakes"))

# -----------------------------------------------------------------------------------
# Create image
# POST https://api.openai.com/v1/images/generations - Creates an image given a prompt.


def generate_image(prompt: str):
  response = openai.Image.create(prompt=prompt, n=1, size="512x512")
  return response.data[0].url


# print(generate_image("Sea Shells On The Sea Shore"))

#-------------------------------------------------------------------------------------
# Create image edit
# POST https://api.openai.com/v1/images/edits - Creates an edited or extended image given an original image and a prompt.


def image_edit(image, mask, prompt):
  response = openai.Image.create_edit(image=open(image, "rb"),
                                      mask=open(mask, "rb"),
                                      prompt=prompt,
                                      n=1,
                                      size="512x512")
  return response.data[0].url


# print(
# image_edit("otter.png", "mask.png", "A cute baby sea otter wearing a beret"))

#--------------------------------------------------------------------------------------
# Create image variation
# POST https://api.openai.com/v1/images/variations - Creates a variation of a given image.


def image_create_variation(image):
  response = openai.Image.create_variation(image=open(image, "rb"),
                                           n=1,
                                           size="512x512")
  return response.data[0].url


# print(image_create_variation("otter.png"))

#----------------------------------------------------------------------------------------
# Create embeddings
# POST https://api.openai.com/v1/embeddings - Creates an embedding vector representing the input text.


def create_embeddings(prompt):
  response = openai.Embedding.create(model="text-embedding-ada-002",
                                     input=prompt)
  return response.data['embedding']


# print(create_embeddings("I am an engineer."))

#------------------------------------------------------------------------------------------
# Create transcription
# POST https://api.openai.com/v1/audio/transcriptions - Transcribes audio into the input language.


def create_transcription_from_audio(audio):
  audio_file = open(audio, "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)
  return transcript.text


# print(create_transcription_from_audio("audio.mp3"))

# --------------------------------------------------------------------------------------------
# Create translation
# POST https://api.openai.com/v1/audio/translations - Translates audio into English.


def translate_audio(audio):
  audio_file = open(audio, "rb")
  transcript = openai.Audio.translate("whisper-1", audio_file)
  return transcript.text


# print(translate_audio("german.m4a"))

# --------------------------------------------------------------------------------------------
# Create moderation.
# POST https://api.openai.com/v1/moderations - Classifies if text violates OpenAI's Content Policy


def moderation_text(input_text):
  response = openai.Moderation.create(input=input_text)
  return response.results


# print(moderation_text("I want to kill all."))

# ----------------------------------------------------------------------------------------------
# Fine Tuning
# List files
# GET https://api.openai.com/v1/files - Returns a list of files that belong to the user's organization.
print(openai.File.list())

# ------------------------------------------------------------------------------------------------
# POST - https://api.openai.com/v1/files
# Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit.


def upload_file(fileName):
  return openai.File.create(file=open(fileName, "rb"), purpose='fine-tune')


# print(upload_file("mydata.jsonl"))

# -------------------------------------------------------------------------------------------------
# DELETE https://api.openai.com/v1/files/{file_id} - Delete a file.


def delete_file(file_id):
  response = openai.File.delete(file_id)
  return response.deleted


# print(delete_file("file-XjGxS3KTG0uNmNOK362iJua3"))

# --------------------------------------------------------------------------------------------------
# GET https://api.openai.com/v1/files/{file_id} - Returns information about a specific file.


def retrieve_file(file_id):
  return openai.File.retrieve(file_id)


# print(retrieve_file("file-XjGxS3KTG0uNmNOK362iJua3"))

# --------------------------------------------------------------------------------------------------
# GET https://api.openai.com/v1/files/{file_id}/content - Returns the contents of the specified file


def file_content(file_id):
  openai.File.download(file_id)


# print(file_content("file-XjGxS3KTG0uNmNOK362iJua3"))

#----------------------------------------------------------------------------------------------------
# Create fine-tune
# POST https://api.openai.com/v1/fine-tune - Creates a job that fine-tunes a specified model from a given dataset.


def create_fine_tune_job(file_id):
  openai.FineTune.create(training_file=file_id)


# print(create_fine_tune_job("file-XjGxS3KTG0uNmNOK362iJua3"))

# ----------------------------------------------------------------------------------------------------
# List fine-tunes
# GET https://api.openai.com/v1/fine-tunes - List your organization's fine-tuning jobs

# print(openai.FineTune.list())

# ----------------------------------------------------------------------------------------------------
# Retrieve fine-tune
# GET https://api.openai.com/v1/fine-tunes/{fine_tune_id} - Gets info about the fine-tune job.


def fine_tune_info(fine_tune_id):
  return openai.FineTune.retrieve(id=fine_tune_id)


# print(fine_tune_info("ft-AF1WoRqd3aJAHsqc9NY7iL8F"))

#------------------------------------------------------------------------------------------------------
# Cancel fine-tune
# POST https://api.openai.com/v1/fine-tunes/{fine_tune_id}/cancel - Immediately cancel a fine-tune job.


def fine_tune_cancel(fine_tune_id):
  return openai.FineTune.cancel(id=fine_tune_id)


# print(fine_tune_cancel("ft-AF1WoRqd3aJAHsqc9NY7iL8F"))

# ------------------------------------------------------------------------------------------------------
# List fine-tune events
# GET https://api.openai.com/v1/fine-tunes/{fine_tune_id}/events - Get fine-grained status updates for a fine-tune job.


def get_fine_tune_events(fine_tune_id):
  return openai.FineTune.list_events(id=fine_tune_id)


# print(get_fine_tune_events("ft-AF1WoRqd3aJAHsqc9NY7iL8F"))

# --------------------------------------------------------------------------------------------------------
# Delete fine-tune model
# DELETE https://api.openai.com/v1/models/{model} - Delete a fine-tuned model. You must have the Owner role in your organization.


def delete_fine_tuned_model(model_id):
  return openai.Model.delete(model_id)


# print(delete_fine_tuned_model("curie:ft-acmeco-2021-03-03-21-44-20"))

#---------------------------------------------------------------------------------------------------------