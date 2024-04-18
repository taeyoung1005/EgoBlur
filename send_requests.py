import requests

# 업로드할 영상 파일 경로
video_file_path = "./test_video.mp4"

# API 엔드포인트 URL
api_url = "http://203.252.230.245:8383/egoblur"

# 파일 업로드
files = {"video": open(video_file_path, "rb")}
response = requests.post(api_url, files=files)

# 응답 확인
if response.status_code == 200:
    print("Video processed successfully")
    # 다운로드 받은 파일을 저장할 경로 및 파일 이름
    download_path = "./test_video_blur.mp4"
    # 파일 저장
    with open(download_path, "wb") as f:
        f.write(response.content)
    print(f"Video saved at {download_path}")
else:
    print("Error processing video")
