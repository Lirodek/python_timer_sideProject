import pymysql  # pymysql 임포트

# 전역변수 선언부
conn = None
cur = None

sql=""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='python', password='3302', db='pythonDB', charset='utf8')	# 접속정보
cur = conn.cursor()	# 커서생성
print('여기부터 시작 ', conn)
sql = "select * from timer"	# 실행할 sql문
cur.execute(sql)	# 커서로 sql문 실행
table_list = cur.fetchall()

conn.commit()	# 저장

conn.close()	# 종료


for table in table_list:
    print(table[0])
    print(table[1])  