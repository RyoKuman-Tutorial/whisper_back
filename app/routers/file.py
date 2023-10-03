import os
import datetime
import secrets

from fastapi import APIRouter, UploadFile
from util.whisper import transcribe_audio

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, 'files/')
AUDIO_DIR = os.path.join(UPLOAD_DIR, 'audios/')
SCRIPT_DIR = os.path.join(UPLOAD_DIR, 'scripts/')


@router.post("/file/")
async def create_upload_file(file: UploadFile):
    file_type = file.filename.split('.')[1]
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    saved_file_name = ''.join([current_time, secrets.token_hex(16)], )
    audio_location = os.path.join(AUDIO_DIR, saved_file_name + "." + file_type)
    script_location = os.path.join(SCRIPT_DIR, saved_file_name + ".txt")
    content = await file.read()

    with open(audio_location, "wb+") as file_object:
        file_object.write(content)

    with open(script_location, "w") as file_object:
        file_object.write(transcribe_audio(audio_location))

    return {"filename": file.filename}
