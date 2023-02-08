from fastapi import FastAPI,File, UploadFile
from starlette.responses import FileResponse 
app1 = FastAPI()

@app1.get("/")
async def read_index():
    return FileResponse('index.html')
@app1.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return 