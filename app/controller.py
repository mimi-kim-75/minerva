from flask import Flask, render_template
from models import show_db


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/index")  # app.route: 라우팅 (교통정리 역할 -> "/"주소로 들어왔을 때 아래의 def를 실행해서 return 한다
def index():
    return render_template("index.html")


@app.route("/join")  # app.route: 라우팅 (교통정리 역할 -> "/"주소로 들어왔을 때 아래의 def를 실행해서 return 한다
def join():
    # 어떤 리퀘스트가 서버로 들어올 때, 해당 리퀘스트를 잘 취합해서 db에 insert하는 것 까지 담당해야 함 = parsing
    # parsing 후 logic을 구현
    # flask form request 찾아볼
    return render_template("join.html")

# join : 신규회원이 입력을 해서 날렷을때 그걸 수집하고 저장하는 로직이 필요


@app.route("/board")  # app.route: 라우팅 (교통정리 역할 -> "/"주소로 들어왔을 때 아래의 def를 실행해서 return 한다
def board():
    return render_template("board.html")


# 라우를 하려면 서버로부터 구동을 해주는 역할을 하는 함수가 필요 -> main.py가 그 역할을 수행
# render_template : flask에서 원하는 파일을 렌더링 해줌
# controller에서 원하는 페이지들을 쭉 추가하면 너무 지저분해짐
# 보통은 app아래에 models라는 디렉토리를 만들고 그 아래에 각각의 로직들을 구현,
# import models 해서 사용


if __name__ == "__main__":
    app.run(debug=True)
