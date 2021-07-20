from flask import Flask
import routes.member as rm
import routes.board as rb

app = Flask(__name__)
app.register_blueprint(rm.bp)
app.register_blueprint(rb.bp)

if __name__ == '__main__':
    app.run()#flask 서버 실행