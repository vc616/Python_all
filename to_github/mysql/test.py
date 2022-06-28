import pymysql

# 打开数据库连接
# db = pymysql.connect("192.168.0.81", "root", "51660180", "dt")
db = pymysql.connect(host= '111.207.218.252', port= 8016, user= 'root', password= '160218vc',db = "test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sq = """INSERT INTO test.温度 (temperature, humidity) VALUES( 88.0, 99.0)"""
# 使用 execute()  方法执行 SQL 查询
try:
    # 执行sql语句
     cursor.execute(sq)
     # 提交到数据库执行
     db.commit()
except:
      # 如果发生错误则回滚
      db.rollback()

# 关闭数据库连接
db.close()