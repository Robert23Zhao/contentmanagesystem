from db.role_dao import RoleDao


class RoleService(object):
    __role_dao = RoleDao()

    def search_list(self):
        """ 查询角色列表 """
        result = self.__role_dao.search_list()
        return result
