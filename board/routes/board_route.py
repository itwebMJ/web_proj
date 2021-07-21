from flask import Blueprint, render_template, request, redirect, session
import board.models.board as b

bp = Blueprint('board', __name__, url_prefix='/board')
board_service = b.BoardService()


@bp.route('/add')
def add_form():
    return render_template('board/form.html')

@bp.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    title = request.form['title']
    content = request.form['content']
    bb = b.Board(writer=id, title=title, content=content)
    board_service.addBoard(bb)
    return redirect('/board/list')

@bp.route('/list')
def list():
    boards = board_service.getAll()
    return render_template('board/list.html', boards=boards)

@bp.route('/detail')
def detail():
    num = request.args.get('num', 0, int)
    bb = board_service.getByNum(num)
    if bb==None:
        return '없는 글'
    else:
        return render_template('board/detail.html', bb=bb)


@bp.route('/edit', methods=["POST"])
def edit():
    num = request.form['num']
    title = request.form['title']
    content = request.form['content']
    board = b.Board(num=num, title=title, content=content)
    board_service.editBoard(board)
    return redirect('/board/list')

@bp.route('/del')
def delete():
    num = request.args.get('num', 0, int)
    board_service.delBoard(num)
    return redirect('/board/list')

@bp.route('/getbywriter', methods=['POST'])
def getbywriter():
    writer = request.form['writer']
    boards = board_service.getByWriter(writer)
    return render_template('board/list.html', boards=boards)

@bp.route('/getbytitle', methods=['POST'])
def getbytitle():
    title = request.form['title']
    boards = board_service.getByTitle(title)
    return render_template('board/list.html', boards=boards)

@bp.route('/getbycontent', methods=['POST'])
def getbycontent():
    content = request.form['content']
    boards = board_service.getByContent(content)
    return render_template('board/list.html', boards=boards)
