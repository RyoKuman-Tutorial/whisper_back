import os
import datetime
import secrets
from fastapi import APIRouter, UploadFile

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, 'files/')


@router.post("/file/")
async def create_upload_file(file: UploadFile):
    file_type = file.filename.split('.')[1]
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    saved_file_name = ''.join([current_time, secrets.token_hex(16)], ) + "." + file_type
    file_location = os.path.join(UPLOAD_DIR, saved_file_name)
    content = await file.read()

    with open(file_location, "wb+") as file_object:
        file_object.write(content)

    return {"filename": file.filename}
