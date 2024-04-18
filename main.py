import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse

from script.egoblur_video import main as egoblur_video_main

app = FastAPI()


@app.post("/egoblur")
async def video_blur(video: UploadFile = File(...)):
    video_input_path = f"input_video/{video.filename}"
    with open(video_input_path, "wb") as buffer:
        buffer.write(video.file.read())
    video_output_path = f"output_video/{video.filename.split('.')[0]}_output.mp4"
    egoblur_video_main(video_input_path, video_output_path)

    return FileResponse(
        video_output_path,
        media_type="video/mp4",
        filename=video_output_path,
    )


@app.get("/")
async def main():
    content = """
    <body>
        <h1>Upload a video to blur the face, carPlate</h1>
        <form action="/egoblur" enctype="multipart/form-data" method="POST">
            <input name="video" type="file">
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(content=content)
