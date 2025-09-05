# 베이스 이미지 (Slim Python)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 설치를 위해 requirements.txt 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# FastAPI 앱 실행 (uvicorn)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
