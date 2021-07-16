from flask import Flask, request, render_template
import vo, model

app = Flask(__name__, template_folder="templates") #flask 객체 생성. 웹 어플리케이션 객체

prod_sercice = model.ProductService()#서비스 객체 생성

@app.route('/')         #라우트 등록. 클라이언트 요청 url 지정
def home():
    return render_template('index.html')

@app.route('/product/add')         #라우트 등록. 클라이언트 요청 url 지정
def add_form():
    return render_template('product/form.html')

@app.route('/product/add', methods=["POST"])
def add():
    name = request.form.get('name', '', str)
    price = request.form.get('price', 0, int)
    amount = request.form.get('amount', 0, int)
    prod = vo.Product(name=name, price=price, amount=amount)
    prod_sercice.addProduct(prod)
    return render_template('index.html', prod=prod)

@app.route('/product/get', methods=["POST"])
def get():
    num = request.form.get('num', 0, int)
    prod = prod_sercice.getProduct(num)
    if prod==None:
        return '없는 제품 번호'
    else:
        return render_template('product/detail.html', prod=prod)

@app.route('/product/list')
def list():
    prods = prod_sercice.getAll()
    return render_template('product/list.html', prods=prods)

@app.route('/product/edit')
def edi_form():
    num = request.args.get('num', 0, int)
    prod = prod_sercice.getProduct(num)
    if prod==None:
        return '없는 제품 번호'
    else:
        return render_template('product/edit_form.html', prod=prod)

@app.route('/product/edit', methods=["POST"])
def edit():
    num = request.form.get('num', 0, int)
    price = request.form.get('price', 0, int)
    amount = request.form.get('amount', 0, int)
    prod = vo.Product(num=num, price=price, amount=amount)
    prod_sercice.editProduct(prod)
    return render_template('index.html')

@app.route('/product/del')
def delete():
    num = request.args.get('num', 0, int)
    prod_sercice.delProduct(num)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
