import pymysql, vo


class ProductDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, prod):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into product_t(name, price, amount) values (%s, %s, %s)"

        vals = (prod.name, prod.price, prod.amount)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def select(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = "select num, name, price, amount from product_t where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            prod = None
            if row != None:
                prod = vo.Product(row[0], row[1], row[2], row[3])
            return prod
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select num, name, price, amount from product_t"
        cur.execute(sql)
        prods = []
        for row in cur:
            prods.append(vo.Product(row[0], row[1], row[2], row[3]))
        self.disconnect()
        return prods

    def update(self, prod):
        self.connect()
        cur = self.conn.cursor()
        sql = "update product_t set price=%s, amount=%s where num=%s"
        vals = (prod.price, prod.amount, prod.num)
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
        sql = "delete from product_t where num=%s"
        vals = (num,)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

class ProductService:
    def __init__(self):
        self.dao = ProductDao()

    def addProduct(self, prod):
        self.dao.insert(prod)

    def getProduct(self, num):
        return self.dao.select(num)

    def getAll(self):
        return self.dao.selectAll()

    def editProduct(self, prods):
        return self.dao.update(prods)

    def delProduct(self, num):
        return self.dao.delete(num)