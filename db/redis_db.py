import redis


try:
    # Redis连接池
    pool = redis.ConnectionPool(host="localhost", port=6379, password="000000", db=1, max_connections=20)

except Exception as e:
    print(e)