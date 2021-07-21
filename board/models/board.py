import pymysql

class Board:
    def __init__(self, num=None, writer=None, w_date=None, title=None, content=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into board(writer, w_date, title, content) values (%s, sysdate(), %s, %s)"

        vals = (board.writer, board.title, board.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByBum(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "select num, writer, w_date, title, content from board where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            bor = None
            if row != None:
                bor = Board(row[0], row[1], row[2], row[3], row[4])
            return bor
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByWriter(self, writer):
        self.connect()
        cur = self.conn.cursor()
        sql = "select num, writer, w_date, title, content from board where writer=%s"
        vals = (writer,)
        cur.execute(sql, vals)
        bor = []
        for row in cur:
            bor.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return bor

    def selectByTitle(self, title):
        self.connect()
        cur = self.conn.cursor()
        content = '%'+title+'%'
        sql = "select num, writer, w_date, title, content from board where title like %s"
        vals = (title,)
        cur.execute(sql, vals)
        bor = []
        for row in cur:
            bor.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return bor

    def selectByContent(self, content):
        self.connect()
        cur = self.conn.cursor()
        content = '%'+content+'%'
        sql = "select num, writer, w_date, title, content from board where content like %s"
        vals = (content,)
        cur.execute(sql, vals)
        bor = []
        for row in cur:
            bor.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return bor

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select num, writer, w_date, title, content from board"
        cur.execute(sql)
        bor = []
        for row in cur:
            bor.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return bor

    def update(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "update board set title=%s, content=%s where num=%s"
        vals = (board.title, board.content, board.num)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delete(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from board where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def addBoard(self, board):
        self.dao.insert(board)

    def getAll(self):
        return self.dao.selectAll()

    def getByNum(self, num):
        return self.dao.selectByBum(num)

    def getByWriter(self, writer):
        return self.dao.selectByWriter(writer)

    def getByTitle(self, title):
        return self.dao.selectByTitle(title)

    def getByContent(self, content):
        return self.dao.selectByContent(content)

    def editBoard(self, board):
        return self.dao.update(board)

    def delBoard(self, num):
        return self.dao.delete(num)