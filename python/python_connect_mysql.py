#数据库连接设置
conn=pymysql.connect(host,user,password,port,db,charset)
#生成游标
cur=conn.cusor(cusor=pymysql.cursors.DictCursor)
#编写sql语句
sql='select * from student'
#执行sql语句
cur.extue(sql)
#获取数据
data=cur.fetchall()
#关闭游标
cur.close()
#关闭连接
conn.close()
