import pymysql

# 打开数据库连接
db = pymysql.connect(host= '111.207.218.252', port= 8016, user= 'root', password= '160218vc',db = "test" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = """SELECT * FROM test.温度 温 where `time` > (NOW()- INTERVAL 12 HOUR )"""

try:
   s = 0
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表      
   results = cursor.fetchall()
   for row in results:
      time = row[0]
      t = row[1]
      h = row[2] 
      # 打印结果
      print( "时间=%s,湿度=%s,温度=%s" % (time, h, t ))
      s = s +1
except:
   print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
print(s)