from flask import Flask, render_template
import routes.mem_route as rm
import routes.board_route as rb
import routes.businfo_route as rbus
import routes.test_route as test
import routes.product_route as prod

app = Flask(__name__, template_folder="templates")
app.secret_key = "cggasadfsgadf" #시크릿키 설정

#생성한 블루프린트 등록
app.register_blueprint(rm.bp)
app.register_blueprint(rb.bp)
app.register_blueprint(rbus.bp)
app.register_blueprint(test.bp)
app.register_blueprint(prod.bp)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()#flask 서버 실행