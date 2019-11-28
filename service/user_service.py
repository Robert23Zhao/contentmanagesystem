from db.user_dao import UserDao


class UserService(object):
    """ 用户服务类 """
    __user_dao = UserDao()

    def login(self, username, password):
        """ 验证用户登录 """
        result = self.__user_dao.login(username, password)
        return result

    def search_user_role(self, username):
        """ 验证用户角色 """
        role = self.__user_dao.search_user_role(username)
        return role

    def insert(self, username, password, email, role_id):
        """ 添加记录 """
        self.__user_dao.insert(username, password, email, role_id)

    def search_count_page(self):
        """ 查询用户总页数 """
        count_page = self.__user_dao.search_count_page()
        return count_page

    def search_list(self, page):
        """ 查询用户分页记录 """
        result = self.__user_dao.search_list(page)
        return result

    def update(self, id, username, password, email, role_id):
        """ 修改用户信息 """
        self.__user_dao.update(id, username, password, email, role_id)

    def delete_by_id(self, id):
        """ 删除用户 """
        self.__user_dao.delete_by_id(id)

    def search_userid(self, username):
        """ 查询用户ID """
        userid = self.__user_dao.search_userid(username)
        return userid
