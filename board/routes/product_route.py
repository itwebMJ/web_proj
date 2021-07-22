from flask import Blueprint, render_template, request, redirect
import board.models.product as prod

bp = Blueprint('product', __name__, url_prefix='/product')    #url 생성기
prod_service = prod.ProductService()

@bp.route('/')
def list():
    prods = prod_service.getAll()
    return render_template('product/list.html', prods=prods)

@bp.route('/add')
def add_form():
    return render_template('product/form.html')

@bp.route('/add', methods=['POST'])
def add():
    upload_path = 'static/product/'
    f = request.files['img_path']  # 이름이 파일이고 타입이 파일인것
    fname = upload_path + f.filename  # 원본 파일 이름
    f.save(fname)
    name = request.form['name']
    price = request.form.get('price', 0, int)
    amount = request.form.get('amount', 0, int)
    img_path = '/' + fname
    p = prod.Product(name=name, price=price, amount=amount, img_path=img_path)
    prod_service.addProduct(p)
    return redirect('/product/')

@bp.route('/get')
def get():
    num = request.args.get('num', 0, int)
    prod = prod_service.getProduct(num)
    return render_template('product/detail.html', prod=prod)



