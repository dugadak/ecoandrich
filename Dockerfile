# 베이스 이미지 선택
FROM python:3.10.0

# 작업 디렉토리 설정
WORKDIR /app

# 소스 코드 복사
COPY . /app

# 의존성 설치
RUN pip install -r requirements.txt

# PostgreSQL 클라이언트 설치
RUN apt-get update && apt-get install -y postgresql-client

# 컨테이너 실행 시 실행할 명령 설정
CMD python manage.py runserver 0.0.0.0:8000
