import openai
from docx import Document


def transcribe_audio(file_path):
    with open(file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']
