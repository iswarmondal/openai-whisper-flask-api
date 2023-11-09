import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def transcribe(audio_path: str):
    audio_file = open(audio_path, "rb")
    response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return response


def translate(audio_path: str):
    audio_file = open(audio_path, "rb")
    response = client.audio.translations.create(model="whisper-1", file=audio_file)
    return response.model_dump_json()
