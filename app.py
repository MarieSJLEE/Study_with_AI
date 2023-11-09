## 여기도 새로운 커밋
from flask import Flask, render_template, request

app = Flask(__name__)

# 텍스트 파일에서 내용을 읽어오는 함수
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# 자기소개서 생성 함수
def generate_introduction(text_content):
    # 여기에서 텍스트 내용을 사용하여 자기소개서를 생성하는 로직을 구현하세요.
    # 예를 들어, 간단한 예제로 "안녕, 나는 [텍스트 내용]에 관심이 있어."를 반환합니다.
    introduction = f"안녕, 나는 {text_content}에 관심이 있어."
    return introduction

@app.route('/', methods=['GET', 'POST'])
def index():
    introduction = ""

    if request.method == 'POST':
        file_path = 'C:\살려줘.txt'  # 여기에 텍스트 파일 경로를 지정하세요
        text_content = read_text_file(file_path)
        introduction = generate_introduction(text_content)

    return render_template('index.html', introduction=introduction)

if __name__ == '__main__':
    app.run(debug=True)
