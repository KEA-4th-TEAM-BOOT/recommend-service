# Python 3.10-slim 이미지를 사용하여 경량화된 이미지를 생성합니다.
FROM python:3.10-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /usr/src/app

# 필요한 패키지 목록을 복사합니다.
COPY requirements.txt ./

# requirements.txt에 명시된 필요한 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션의 모든 소스 코드를 복사합니다.
COPY . .

# 컨테이너 외부로 포트 8001을 열어둡니다.
EXPOSE 8001

# 컨테이너가 시작될 때 실행할 명령어를 설정합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
