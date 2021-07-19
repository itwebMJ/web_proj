import pymysql, MemberVo


class MemberDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into member(id, pwd, name, email) values (%s, %s, %s, %s)"

        vals = (mem.id, mem.pwd, mem.name, mem.email)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def select(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = "select id, pwd, name, email from member where id=%s"
        vals = (id,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            mem = None
            if row != None:
                mem = MemberVo.Member(row[0], row[1], row[2], row[3])
            return mem
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select id, pwd, name, email from member"
        cur.execute(sql)
        mem = []
        for row in cur:
            mem.append(MemberVo.Member(row[0], row[1], row[2], row[3]))
        self.disconnect()
        return mem

    def update(self, mem):
        self.connect()
        cur = self.conn.cursor()
        sql = "update member set pwd=%s, name=%s, email=%s where id=%s"
        vals = (mem.pwd, mem.name, mem.email, mem.id)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delete(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = "delete from member where id=%s"
        vals = (id,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

class MemberService:
    def __init__(self):
        self.dao = MemberDao()

    def join(self, mem):
        self.dao.insert(mem)

    def getMember(self, id):
        return self.dao.select(id)

    def getAll(self):
        return self.dao.selectAll()

    def editMember(self, mem):
        return self.dao.update(mem)

    def delMember(self, id):
        return self.dao.delete(id)