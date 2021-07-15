from flask import Flask, request, render_template
import vo

app = Flask(__name__, template_folder="templates") #flask 객체 생성. 웹 어플리케이션 객체

@app.route('/')         #라우트 등록. 클라이언트 요청 url 지정
def my_root():
    return 'hello flask'

@app.route('/test')
def my_test():
    return 'flask test'

#@app.route('/form1', methods=['GET'])
@app.route('/form1')
def test2():
    return render_template('form1.html')

@app.route('/form1', methods=['POST'])
def form1():
    id = request.form['id']
    pwd = request.form['pwd']
    return 'id:%s, pwd:%s'%(id, pwd)

@app.route('/get-test')     #http://127.0.0.1:5000/get-test?name=aaa&age=12
def get_test():
    name = request.args.get("name", "", str)
    age = request.args.get("age", 0, int)
    return 'name:%s, age:%s'%(name, age)

@app.route('/join')
def join_form():
    return render_template('joinForm.html')

@app.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    hobby = request.form['hobby']
    grade = request.form['grade']
    msg = request.form['msg']

    m = vo.Member(id, pwd, name, email, gender, hobby, grade, msg)
    #return render_template('join_result.html', r_id=id, r_pwd=pwd, r_name=name, r_email=email)
    return render_template('join_result.html', m=m)


if __name__ == '__main__':
    app.run()

