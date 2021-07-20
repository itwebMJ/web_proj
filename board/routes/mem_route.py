from flask import Blueprint, render_template, request, redirect, session
import board.models.member as m

bp = Blueprint('member', __name__, url_prefix='/member')

mem_service = m.MemberService()
bp.secret_key = "cggasadfsgadf" #시크릿키 설정

@bp.route('/join')
def join_form():
    return render_template('member/join.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form.get('id', '', str)
    pwd = request.form.get('pwd', '', str)
    name = request.form.get('name', '', str)
    email = request.form.get('email', '', str)
    mem = m.Member(id=id, pwd=pwd, name=name, email=email)
    mem_service.join(mem)
    return redirect('/')


@bp.route('/login')
def login_form():
    return render_template('member/login.html')

@bp.route('/login', methods=['POST'])
def login():
    msg = ''
    path = 'member/login.html'
    id = request.form['id']
    pwd = request.form['pwd']
    m = mem_service.getMember(id)
    if m == None:
        msg = '없는 아이디'
    else:
        if pwd == m.pwd:
            session['id'] = id
            path = 'index.html'
            msg = '로그인 성공'
        else:
            msg = '패스워드 불일치'
    return render_template(path, msg=msg)

@bp.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id', None)
    return redirect('/')

@bp.route('/getmember')
def getMember():
    if 'id' in session:
        id = session['id']
    mem = mem_service.getMember(id)
    if mem==None:
        return '없는 아이디'
    else:
        return render_template('member/detail.html', mem=mem)



@bp.route('/edit', methods=["POST"])
def mem_edit():
    id = request.form['id']
    pwd = request.form['pwd']
    # name = request.form['name']
    # email = request.form['email']
    mem = m.Member(id=id, pwd=pwd)
    mem_service.editMember(mem)
    return redirect('/')

@bp.route('/del')
def mem_delete():
    if 'id' in session:
        id = session['id']
    mem_service.delMember(id)
    session.pop('id', None)
    return redirect('/')




if __name__ == '__main__':
    bp.debug = True
    bp.run()