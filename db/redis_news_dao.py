import redis
from db.redis_db import pool


class RedisNewsDao(object):

    def insert(self, id, title, username, type, content, is_top, create_time):
        """ 写入新闻内容 """
        con = redis.Redis(connection_pool=pool)
        try:
            con.hmset(id, {
                "title": title,
                "username": username,
                "type": type,
                "content": content,
                "is_top": is_top,
                "create_time": create_time
            })
            if is_top == 0:
                con.expire(id, 24*60*60)
        except Exception as e:
            print(e)
        finally:
            del con

    def delete_cache(self, id):
        """ 删除缓存的新闻 """
        con = redis.Redis(connection_pool=pool)
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con
