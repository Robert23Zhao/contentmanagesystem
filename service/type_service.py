from db.type_dao import TypeDao


class TypeService(object):
    __type_dao = TypeDao()

    def search_list(self):
        """ 查询新闻类型列表 """
        result = self.__type_dao.search_list()
        return result
