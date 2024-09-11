FROM python:3.12.6

# 작업 디렉토리 설정
WORKDIR /app/

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
# COPY app.py .
COPY . .



EXPOSE 8000

# 컨테이너가 실행할 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
