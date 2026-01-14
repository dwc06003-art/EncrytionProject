
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from cipher_lib.caesar_cipher_v2 import caesar_cipher
from cipher_lib.vigenere_cipher import vigenere_cipher
from cipher_lib.playfare_cipher import

# FastAPI 인스턴스 생성
app = FastAPI()

# 템플릿 엔진 설정 및 templates 폴더 경로 지정
templates = Jinja2Templates(directory="templates")


# 루트 경로("/jhello")에 GET 요청이 들어오면 실행될 함수 정의
@app.get("/jhello")
def json_hello():
    return {"message": "Hello, World!"}


# 별도의 HTML 파일을 사용해서 웹 페이지를 렌더링
# 보통 Jinja2 템플릿 엔진을 사용하며, templates 폴더를 만들어 HTML 파일을 두고 렌더링
@app.get("/j2hello", response_class=HTMLResponse)
# Request : 클라이언트가 서버로 보낸 HTTP 요청 전체를 담은 특별한 변수(객체)
def jinja2_hello(request: Request):
    # TemplateResponse(템플릿파일명, 템플릿에_전달할_데이터)
    # 템플릿 컨텍스트 - HTML 안에서 사용할 수 있는 변수들의 집합
    # json : 자바스크립트를 이용해서 데이터를 표현한는 형식
    # {}에 '키:값' 쌍으로 데이터들을 정의
    return templates.TemplateResponse("j2hello.html",
                            {"request": request, "message": "Hello, World!"})


# GET 요청: 로그인 폼 보여주기
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# POST 요청: 폼 데이터 처리
@app.post("/login", response_class=HTMLResponse)
# username, password는 Form 데이터에서 문자열 타입으로 필수 입력 값이다
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # username과 password 값을 템플릿으로 전달
    form = await request.form()
    # 암호화 처리
    caesar_encrypted = caesar_cipher(password, 3)
    secret_key = 'secret is beautiful'
    vigenere_encrypted = vigenere_cipher(password, secret_key)


    return templates.TemplateResponse("loginok.html", {
        "request": request, "form" : form, "username": username, "password": password,
        "caesar_encrypted" :caesar_encrypted, "vigenere_encrypted": vigenere_encrypted
    })


# 스크립트를 직접 실행할 때만 서버 실행
if __name__ == "__main__":
    import uvicorn  # uvicorn을 직접 임포트해서 사용
    uvicorn.run('02Jinja2_FastAPI:app', host="0.0.0.0", port=8000, reload=True)