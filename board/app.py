from flask import Flask, request, render_template
import routes.mem_route as rm
import routes.board_route as rb

app = Flask(__name__, template_folder="templates")
app.register_blueprint(rm.bp)
app.register_blueprint(rb.bp)
app.secret_key = "cggasadfsgadf" #시크릿키 설정

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()#flask 서버 실행