FROM python:3.12.6

# 작업 디렉토리 설정
WORKDIR /app/

# 시스템 종속성 설치 (libGL 포함)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    # 기타 필요한 패키지들
    && rm -rf /var/lib/apt/lists/*



# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# 애플리케이션 코드 복사
# COPY app.py .
COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# 컨테이너가 실행할 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
