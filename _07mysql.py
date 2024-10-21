from pymysql import Connection

conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    autocommit=True
)

print(conn.get_server_info())
cursor=conn.cursor()
conn.select_db("sqldemo")
cursor.execute("select * from user")
results=cursor.fetchall()
print(results)
sql='insert into user(id,username,password) values (4,"马六","147852")'
cursor.execute(sql)
conn.close()