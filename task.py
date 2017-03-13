import redis
from config import config

RUN_LEVEL = 'development'

redis_pool = redis.ConnectionPool(host='localhost', port=config[RUN_LEVEL].REDIS_PORT,
                            db=config[RUN_LEVEL].REDIS_DB)
db_redis = redis.Redis(connection_pool=redis_pool)

while True:
    result = db_redis.brpop(config[RUN_LEVEL].REDIS_REQ_QUEUE, 0)
    print(result)

