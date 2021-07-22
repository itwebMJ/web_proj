from flask import Blueprint, render_template, request, redirect, session
import matplotlib.pyplot as plt

bp = Blueprint('test', __name__, url_prefix='/test')    #url 생성기



@bp.route('/graph')
def graph():
    img_path = 'static/graph/my_plot.png'

    x = [1, 2, 3, 4]
    y = [3, 8, 5, 6]
    fig, ax = plt.subplots() #그래프 그릴 프래임. 그래프를 분할 할때도 씀
    #fig, _ = plt.subplots() 사용 안할때는 ' _ ' 로 임시 저장해 사용
    plt.plot(x, y)  #그래프 그림
    fig.savefig(img_path)
    img_path = '/' + img_path
    return render_template('test/test.html', img_path=img_path)

@bp.route('/upload')
def upload_form():
    return render_template('test/form.html')

@bp.route('/upload', methods=['POST'])
def upload():
    upload_path = 'static/img/'
    f = request.files['file']   #이름이 파일이고 타입이 파일인것
    fname = upload_path+f.filename      #원본 파일 이름
    f.save(fname)
    fname = '/' + fname
    return render_template('test/test.html', img_path=fname)