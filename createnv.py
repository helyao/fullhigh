import pymysql
from config import config

RUN_LEVEL = 'development'

############ MySQL ############

print('- INIT MySQL... -')

mysql_conn = pymysql.connect(host='localhost',
                             port=config[RUN_LEVEL].MYSQL_PORT,
                             user=config[RUN_LEVEL].MYSQL_USER,
                             passwd=config[RUN_LEVEL].MYSQL_PASSWD,
                             db=config[RUN_LEVEL].MYSQL_DB)
db_mysql = mysql_conn.cursor()

# Create log file - store all equipments message
log_name = config[RUN_LEVEL].MYSQL_LOG_TAB

drop_table = "DROP TABLE IF EXISTS {0}".format(log_name)

db_mysql.execute(drop_table)

create_table = "CREATE TABLE {0}(" \
               "equip_ip INT(10) UNSIGNED, " \
               "equip_port MEDIUMINT UNSIGNED, " \
               "time TIMESTAMP(3) DEFAULT NOW(3), " \
               "message VARCHAR(16))".format(log_name)

db_mysql.execute(create_table)

"""
# Test for log table

index_record = "INSERT INTO {0}(equip_ip, equip_port, message) VALUES(INET_ATON('{1}'), {2}, '{3}')".format(log_name, '192.168.1.10', 10010, 'test')

print(index_record)

db_mysql.execute(index_record)

# Commit

mysql_commit = "commit"
db_mysql.execute(mysql_commit)

"""

print('- MySQL INIT END -')