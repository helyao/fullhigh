import json
import redis
import socket
from common import print_error
from config import config, RUN_LEVEL

# Redis
redis_pool = redis.ConnectionPool(host='localhost', port=config[RUN_LEVEL].REDIS_PORT,
                            db=config[RUN_LEVEL].REDIS_DB)
db_redis = redis.Redis(connection_pool=redis_pool)

# UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("0.0.0.0", config[RUN_LEVEL].UDP_SND_PORT))

while True:
    result = db_redis.brpop(config[RUN_LEVEL].REDIS_SND_QUEUE, 0)
    record = json.loads(result[1].decode(encoding='UTF-8'))
    print(record)
    try:
        udp.sendto(record['cmd'].encode('latin1'), (record['ip'], record['port']))
    except Exception as ex:
        print_error(ex)