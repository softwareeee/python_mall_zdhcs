from Public.mysql_operate import MysqlDb
from Public.mysql_operate import DB_CONF
if __name__ == '__main__':
    db = MysqlDb(DB_CONF)
    print(db.select_db("SELECT * FROM eq_mall_info"))


