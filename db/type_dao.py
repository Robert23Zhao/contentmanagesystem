from db.mysql_db import pool


class TypeDao(object):

    def search_list(self):
        """ 查询新闻类型列表 """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id,type FROM t_type ORDER BY id;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
