# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
# 한글처리 (charset = 'utf8')

# ===== default =====
cur         = None
con         = None
# ===================


def open():
    global cur, con
    con = pymysql.connect(host='localhost', user='python', password='3302', db='pythonDB', charset='utf8') 
    cur = con.cursor() 

def test():
    open()
    global con, cur
    
    sql = "SELECT * FROM timer" 

    cur.execute(sql) 
    res = cur.fetchall() 
    close()
    return res
    

def close():
    global con
    con.commit() 
    con.close() 
# class Database:
#     def openDB():
#         global cur
#         global con
#         # 데이터베이스 연결
#         con = pymysql.connect(host='localhost', user='python', password='3302', db='pythonDB', charset='utf8') 
    
#         # STEP 3: Connection 으로부터 Cursor 생성
#         cur = con.cursor()
        

#     # 반복되는 알람
#     def insert_recurring_alarm():
        
#         # SQL문 실행 및 Fetch
#         sql = "SELECT * FROM timer"
#         cur.execute(sql)
#         result = cur.fetchall()
#         print(result)
#         con.close()
#         # 데이타 Fetch return
    