from db.mysql_db import pool


class UserDao(object):
    """ 用户执行SQL语句类 """
    def login(self, username, password):
        """
        验证用户登录
        :param username:用户名
        :param password: 密码
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s and AES_DECRYPT(UNHEX(password),'HelloWorld')=%s;"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_user_role(self, username):
        """ 验证用户角色 """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id=r.id WHERE u.username=%s;"
            cursor.execute(sql, (username, ))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def insert(self, username, password, email, role_id):
        """ 添加记录 """
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user(username,password,email,role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_count_page(self):
        """ 查询用户总页数 """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_user"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_list(self, page):
        """ 查询用户分页记录 """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT u.id,u.username,r.role " \
                  "FROM t_user u JOIN t_role r " \
                  "ON u.role_id=r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update(self, id, username, password, email, role_id):
        """ 修改用户信息 """
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user SET username=%s," \
                  "password=HEX(AES_ENCRYPT(%s,'HelloWorld'))," \
                  "email=%s,role_id=%s " \
                  "WHERE id=%s"
            cursor.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_by_id(self, id):
        """ 删除用户 """
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_userid(self, username):
        """ 查询用户ID """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id FROM t_user WHERE username=%s"
            cursor.execute(sql, [username])
            userid = cursor.fetchone()[0]
            return userid
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
