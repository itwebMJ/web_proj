from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates") #flask 객체 생성. 웹 어플리케이션 객체

@app.route('/')         #라우트 등록. 클라이언트 요청 url 지정
def root():
    return render_template('index.html')

@app.route('/member/join')
def join_form():
    return render_template('member/join.html')

@app.route('/member/login')
def login_form():
    return render_template('member/login.html')

@app.route('/get-test')
def get_test():
    id = request.args.get("id", "", str)
    pwd = request.args.get("pwd", "", str)
    return id+' / '+pwd

@app.route('/member/login', methods=["POST"])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    return render_template('member/login_result.html', id=id, pwd=pwd)

@app.route('/view-test1')
def view_test():
    id = 'aaa'
    pwd = '111'
    return render_template('test1.html', a=id, b=pwd)

if __name__ == '__main__':
    app.run()
