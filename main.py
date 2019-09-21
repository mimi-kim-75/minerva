# flask는 디렉토리 구조를 짜는 것이 중요
# 디렉토리 구조를 잘못 짤 경우 구동이 되지 않음 (페이지들의 얼개)

from app import controller


if __name__ == "__main__":
    controller.app.run(port=8888)

    # run()안에 입력이 없을 경우 : local host: 5000번 포트로 열어줌
    # 실행 되면 서버가 켜지고 중지 시키면 서버가 죽음 (port가 닫힘)