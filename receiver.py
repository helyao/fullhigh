import redis
import socket
import pymysql
from common import print_error
from config import config, RUN_LEVEL

# commit frequency
COMMIT_COUNT = 0
COMMIT_FRE = 10


def log_write(addr, mess):
    global COMMIT_COUNT, COMMIT_FRE
    COMMIT_COUNT = (COMMIT_COUNT + 1) % COMMIT_FRE
    record = "INSERT INTO {0}(equip_ip, equip_port, message) VALUES(INET_ATON('{1[0]}'), {1[1]}, '{2}')".format(config[RUN_LEVEL].MYSQL_LOG_TAB, addr, mess.decode('latin1'))
    print(record)
    db_mysql.execute(record)
    if COMMIT_COUNT == 0:
        print('commit')
        db_mysql.execute('commit')
    # select hex(message) from log_tab where equip_ip=INET_ATON('192.168.1.10')
    type = mess[1]
    if type == 2:   # req package
        ccc
    elif type == 3: # ack package
        db_redis.lpush(config[RUN_LEVEL].REDIS_ACK_QUEUE, 'ack task {}'.format(COMMIT_COUNT))
    else:           # status package
        pass

# Redis
redis_pool = redis.ConnectionPool(host='localhost', port=config[RUN_LEVEL].REDIS_PORT,
                            db=config[RUN_LEVEL].REDIS_DB)
db_redis = redis.Redis(connection_pool=redis_pool)

# MySQL
mysql_conn = pymysql.connect(host='localhost', port=config[RUN_LEVEL].MYSQL_PORT,
                             user=config[RUN_LEVEL].MYSQL_USER,
                             passwd=config[RUN_LEVEL].MYSQL_PASSWD,
                             db=config[RUN_LEVEL].MYSQL_DB)
db_mysql = mysql_conn.cursor()

# UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("0.0.0.0", config[RUN_LEVEL].UDP_REC_PORT))


while True:
    try:
        message, address = udp.recvfrom(1024)
        print('IP = "{1[0]}" & PORT = {1[1]} SAY: \n\t{0}'.format(message, address))
        log_write(address, message)
    except Exception as ex:
        print_error(ex)

