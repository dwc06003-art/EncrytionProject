# fastapi 패키지에서 FastAPI 클래스를 가져옵니다.
# FastAPI는 웹 API 서버를 만들기 위한 핵심 클래스입니다.
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse

# FastAPI 애플리케이션 객체를 생성합니다.
# 이 객체(app)가 전체 웹 서버를 대표하며,
# 라우팅(URL 처리), 미들웨어, 설정 등을 관리합니다.
app = FastAPI()

# HTTP GET 요청을 처리하는 엔드포인트(경로)를 정의합니다.
# "/" 는 서버의 루트(root) 경로를 의미합니다.
# 즉, 브라우저에서 http://localhost:8000/ 로 접속하면
# 이 함수가 실행됩니다.
@app.get("/")
async def json_hello():
    """
    이 함수는 루트 경로("/")로 GET 요청이 들어왔을 때 실행됩니다.

    async 키워드:
    - 비동기 함수임을 의미합니다.
    - FastAPI는 비동기 처리를 지원하여
      동시에 많은 요청을 효율적으로 처리할 수 있습니다.

    함수 이름(json_hello):
    - 함수 이름은 내부적으로 사용되며
      실제 URL과 직접적인 관계는 없습니다.
    """

    # 파이썬 딕셔너리를 반환합니다.
    # FastAPI는 이를 자동으로 JSON 형식으로 변환하여
    # 클라이언트(브라우저, 앱 등)에 응답합니다.
    return {"message": "Hello, World!"}

@app.get("/thello", response_class=PlainTextResponse)
def text_hello():
    # 텍스트로 응답
    return "Hello, World!"

@app.get("/hhello", response_class=HTMLResponse)
def html_hello():
    # html로 응답
    html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Hello Page</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>FastAPI로 만든 HTML 페이지입니다.</p>
            </body>
        </html>
        """
    return html_content


# 스크립트를 직접 실행할 때만 서버 실행
if __name__ == "__main__":
    import uvicorn  # uvicorn을 직접 임포트해서 사용
    uvicorn.run('01Hello_FastAPI:app', host="0.0.0.0", port=8000, reload=True)