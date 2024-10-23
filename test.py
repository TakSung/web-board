from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="홈 페이지", message="플라스크 웹 애플리케이션에 오신 것을 환영합니다!")

@app.route('/redirect_example')
def redirect_example():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)