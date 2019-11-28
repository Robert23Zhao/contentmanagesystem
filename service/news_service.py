from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewsDao


class NewsService(object):
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()

    def search_unreview_list(self, page):
        """ 查询待审批新闻列表 """
        result = self.__news_dao.search_unreview_list(page)
        return result

    def search_unreview_count_page(self):
        """ 查询待审批新闻的总页数 """
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    def update_unreview_news(self, id):
        """ 审批新闻 """
        self.__news_dao.update_unreview_news(id)

    def search_list(self, page):
        """ 查询新闻列表 """
        result = self.__news_dao.search_list(page)
        return result

    def search_count_page(self):
        """ 查询新闻总页数 """
        count_page = self.__news_dao.search_count_page()
        return count_page

    def delete_by_id(self, id):
        """ 删除新闻 """
        content_id = self.__news_dao.search_content_id(id)
        self.__news_dao.delete_by_id(id)
        self.__mongo_news_dao.delete_by_id(content_id)

    def insert(self, title, editor_id, type_id, content, is_top):
        """ 添加新闻 """
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    def search_cache(self, id):
        """ 查找用户缓存的记录 """
        result = self.__news_dao.search_cache(id)
        return result

    def cache_news(self, id, title, username, type, content, is_top, create_time):
        """ 向Redis里写入数据 """
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    def delete_cache(self, id):
        """ 删除缓存的新闻 """
        self.__redis_news_dao.delete_cache(id)

    def search_by_id(self, id):
        """ 根据id查找新闻 """
        result = self.__news_dao.search_by_id(id)
        return result

    def update(self, id, title, type_id, content, is_top):
        """ 更改新闻"""
        content_id = self.__news_dao.search_content_id(id)
        self.__mongo_news_dao.update(content_id, title, content)
        self.__news_dao.update(id, title, type_id, content_id, is_top)
        self.delete_cache(id)

    def search_content_by_id(self, id):
        """ 查询正文id """
        content = self.__mongo_news_dao.search_content_by_id(id)
        return content
