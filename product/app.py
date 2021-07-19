from flask import Flask, request, render_template, redirect

'''
테이블 생성
vo(클래스명 : 테이블이름 / 멤버변수 : 컬럼이름) 작성
dao(객체로 db작업) 작성
insert(): 객체 하나를 db 테이블에 한 줄 추가 회원등록
select(primary key) : 한개 검색. primary key는 중복 허용 안하므로 1개가 검색되든지 없든지 
selectAll() : 조건없이 전체검색 ; 전체목록
update(): 수정, 조건(where)을 만족하는 행에 대해서 원하는 컬럼값 수정 ; 수정
delete() : 삭제, 조건(where)을 만족하는 행 삭제
<db작업단계>
db connection 수립(db 서버 시스템에 로그인해서 서버 수립)
service 작성
	외부에 기능 제공, app.py(controller)에 사용할 기능을 정의
app.py(controller) 작성
플라스크 객체 생성
route()를 이용해서 사용자에게 제공할 url 등록 get post 
등록한 url마다 실행할 함수를 작성 : 실행할 코드와 보여줄 뷰 페이지 생성
뷰 페이지로 사용할 html 파일 작성

'''

import vo, model, MemberVo, MemberModel

app = Flask(__name__, template_folder="templates") #flask 객체 생성. 웹 어플리케이션 객체

prod_sercice = model.ProductService()#서비스 객체 생성
mem_sercice = MemberModel.MemberService()

@app.route('/')         #라우트 등록. 클라이언트 요청 url 지정
def home():
    return render_template('index.html')

#=========product========
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

# list에서 번호 누르면 detail.html 페이지
@app.route('/product/detail')
def detail():
    num = request.args.get('num', 0, int)
    prod = prod_sercice.getProduct(num)
    if prod==None:
        return '없는 제품 번호'
    else:
        return render_template('product/detail.html', prod=prod)

#=========member========
@app.route('/member/join')
def join_form():
    return render_template('member/join.html')

@app.route('/member/join', methods=["POST"])
def join():
    id = request.form.get('id', '', str)
    pwd = request.form.get('pwd', '', str)
    name = request.form.get('name', '', str)
    email = request.form.get('email', '', str)
    mem = MemberVo.Member(id=id, pwd=pwd, name=name, email=email)
    mem_sercice.join(mem)
    return redirect('/')

@app.route('/member/login')
def login_form():
    return render_template('member/login.html')

@app.route('/member/login', methods=["POST"])
def login():
    id = request.form.get('id', '', str)
    pwd = request.form.get('pwd', '', str)
    mem = mem_sercice.getMember(id)
    return render_template('member/login.html')

@app.route('/member/list')
def mem_list():
    mem = mem_sercice.getAll()
    return render_template('member/list.html', members=mem)

@app.route('/member/get', methods=["POST"])
def mem_get():
    id = request.form.get('id', '', str)
    mem = mem_sercice.getMember(id)
    if mem==None:
        return '없는 아이디'
    else:
        return render_template('member/detail.html', mem=mem)

@app.route('/member/edit')
def mem_edit_form():
    id = request.args.get('id',  '', str)
    mem = mem_sercice.getMember(id)
    if mem==None:
        return '없는 아이디'
    else:
        return render_template('member/detail.html', mem=mem)

@app.route('/member/edit', methods=["POST"])
def mem_edit():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    mem = MemberVo.Member(id=id, pwd=pwd, name=name, email=email)
    mem_sercice.editMember(mem)
    return redirect('/')

@app.route('/member/del')
def mem_delete():
    id = request.args.get('id',  '', str)
    mem_sercice.delMember(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
