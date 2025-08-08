# Shorty - URL 단축기

![CI/CD Pipeline](https://github.com/USERNAME/REPO_NAME/actions/workflows/ci.yml/badge.svg)

클라우드 네이티브 아키텍처의 핵심 개념을 적용하여 개발한 MSA 기반 URL 단축 서비스.

## 🚀 프로젝트 개요

이 프로젝트는 마이크로서비스 아키텍처(MSA), 컨테이너(Docker), CI/CD(GitHub Actions) 등 클라우드 네이티브 기술 스택을 직접 경험하고 구현하는 것을 목표로 합니다. 사용자는 웹 페이지를 통해 긴 URL을 짧게 줄일 수 있으며, 생성된 단축 URL로 접속 시 원래의 페이지로 즉시 리다이렉션됩니다.

## ✨ 핵심 기능

-   **URL 단축**: 긴 URL을 입력하여 짧고 고유한 URL 코드를 생성합니다.
-   **리다이렉션**: 생성된 단축 URL 접속 시 원래 URL로 빠르게 이동시킵니다.
-   **자동화된 빌드/배포**: `main` 브랜치에 코드 푸시 시 자동으로 Docker 이미지를 빌드하여 GitHub Container Registry에 게시합니다.

## 🛠️ 아키텍처 및 기술 스택

이 프로젝트는 명확하게 분리된 3개의 서비스가 Docker 컨테이너 환경에서 유기적으로 동작하도록 설계되었습니다.

| 구분 | 역할 | 주요 기술 |
| :--- | :--- | :--- |
| **Frontend** | 사용자 인터페이스 제공, API 요청 | React.js, Vite, Axios, Nginx |
| **Backend** | 핵심 비즈니스 로직, API 제공 | Python, FastAPI, Uvicorn |
| **Database** | URL 매핑 정보 저장 | Redis |
| **DevOps** | 컨테이너화, CI/CD, 오케스트레이션 | Docker, Docker Compose, GitHub Actions |

### 동작 과정 (End-to-End Flow)

사용자가 URL 단축을 요청했을 때, 데이터는 아래와 같은 순서로 흐릅니다.

1.  **[사용자]** 웹 브라우저(`http://localhost`)를 통해 프론트엔드 UI에 접속합니다.
2.  **[Frontend: React]** 사용자가 긴 URL을 입력하고 '단축하기' 버튼을 클릭하면, Axios를 통해 `/api/url` 로 POST 요청을 보냅니다.
3.  **[Frontend: Nginx]** 프론트엔드 컨테이너의 Nginx는 `/api`로 시작하는 이 요청을 리버스 프록시 설정을 통해 백엔드 컨테이너(`http://backend:8000`)로 전달합니다.
4.  **[Backend: FastAPI]** 백엔드 서버는 요청을 받아, 입력된 URL을 기반으로 고유한 단축 코드를 생성합니다.
5.  **[Backend/Database: Redis]** 생성된 단축 코드와 원본 URL을 Key-Value 쌍으로 Redis 데이터베이스에 저장합니다.
6.  **[Backend: FastAPI]** 저장 후, 생성된 단축 코드를 JSON 형식으로 프론트엔드에 응답합니다.
7.  **[Frontend: React]** 응답받은 단축 코드를 화면에 표시하여 사용자가 확인할 수 있게 합니다.

## ⚙️ 로컬에서 실행하기

이 프로젝트를 로컬 환경에서 실행하기 위해서는 Docker와 Docker Compose가 설치되어 있어야 합니다.

1.  **레포지토리 클론:**
    ```bash
    git clone [https://github.com/USERNAME/REPO_NAME.git](https://github.com/USERNAME/REPO_NAME.git)
    cd REPO_NAME
    ```

2.  **Docker Compose 실행:**
    프로젝트 루트 디렉토리에서 아래 명령어를 실행하면 모든 서비스가 빌드되고 실행됩니다.
    ```bash
    docker-compose up --build
    ```

3.  **애플리케이션 접속:**
    웹 브라우저를 열고 `http://localhost` 로 접속합니다.

## 🤖 자동화 (CI/CD)

이 프로젝트는 GitHub Actions를 통해 CI/CD 파이프라인이 구축되어 있습니다.

-   **Trigger**: `main` 브랜치에 코드가 푸시될 때마다 워크플로우가 자동으로 실행됩니다.
-   **Jobs**:
    -   `build-and-push-backend`: 백엔드 코드를 Docker 이미지로 빌드하여 GHCR에 푸시합니다.
    -   `build-and-push-frontend`: 프론트엔드 코드를 Docker 이미지로 빌드하여 GHCR에 푸시합니다.
-   **확인**: 워크플로우의 실행 상태는 레포지토리의 'Actions' 탭에서, 푸시된 이미지는 'Packages' 탭에서 확인할 수 있습니다.