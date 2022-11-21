# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
# 한글처리 (charset = 'utf8')

# ===== default =====
cur         = None
con         = None
# ===================

# Database를 열어주는 함수
def _open():
    global cur, con
    con = pymysql.connect(host='', user='', password='', db='', charset='utf8') 
    cur = con.cursor() 

# 현재 데이터베이스 안의 루프함수와, 날짜 함수 안의 원하는 데이터를 가져옵니다.
def test(test):
    _open()
    global con, cur
    sql = """	
        SELECT 
        A.timer_hour      
      , A.timer_minute
      , A.LNK
      FROM (
         SELECT  timer_hour
                    , timer_minute
                    , LNK
                FROM selectday 
                WHERE USER = 'Lirodek'
                AND TIMER_DATE = DATE_FORMAT(now(), '%Y%m%d')
            UNION 
            SELECT timer_hour
                    , timer_minute 
                    , LNK
                FROM loof
                WHERE USER = 'lirodek'
                AND """+test+""" = 1
            ) A
            WHERE CONCAT(A.timer_hour , A.TIMER_MINUTE) > CONCAT(DATE_FORMAT(NOW(), '%H%i'))
            AND TIMER_HOUR >= HOUR(NOW())
            ORDER BY A.timer_hour , A.TIMER_MINUTE
         LIMIT 1
        """
    cur.execute(sql) 
    res = cur.fetchall() 

    _close()
    return res
# 특정날짜에 해당하는 칼럼의 갯수를 가져옵니다.
def selectDayCount():
    global cur
    _open()
    sql = """
        SELECT COUNT(*) as count
        FROM selectday
        WHERE USER='lirodek'
		AND   timer_date > DATE_FORMAT(now(), '%Y%m%d') 
    """
    cur.execute(sql)
    res = cur.fetchall()
    _close()
    return res

# 특정날짜에 동작하는 알람만 가져옵니다.
def selectDayTimer():
    _open()
    global con, cur
    sql = """
        SELECT 
		  key_num
		, timer_date
		, timer_hour
		, timer_minute
		, lnk
		FROM selectday
		WHERE USER='lirodek'
		AND   timer_date > DATE_FORMAT(now(), '%Y%m%d') 
	    ORDER BY timer_date
    """
    cur.execute(sql)
    res = cur.fetchall()
    _close()
    return res

# 특정날짜에만 동작하는 알람을 설정해줍니다.
def insertToDayTimer(data):
    _open()
    sql = """
        INSERT INTO selectday
		(USER, TIMER_DATE, TIMER_HOUR, TIMER_MINUTE, LNK)
		VALUES 
    """ + data
    cur.execute(sql) 
    res = cur.fetchall() 
    _close()
    return res

# 특정요일에 반복하는 알람을 생성합니다.
def insertLoof(values):
    _open()
    sql = """
        INSERT INTO loof 
        (USER, timer_hour, timer_minute, lnk, sun, mon, tue, wed, thu, fri, sat)
        VALUES """ + values
    cur.execute(sql) 
    res = cur.fetchall() 
    _close()
    return res
    
# 데이터베이스를 닫아줍니다.
def _close():
    global con
    con.commit() 
    con.close() 
# class Database:
#     def _openDB():
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
#         con._close()
#         # 데이타 Fetch return
    
