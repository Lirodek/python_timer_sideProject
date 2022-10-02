### intro.
## Date : 2020. 11. 26
## Editer : 성원경 선생님 / 경기기계공업고등학교

### 3. 유튜브 매크로 알람 시계

### 디지털 시계 코드 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time
import pyautogui
import clipboard

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

macro = True
# ========== 전역 변수 이 값을 바꿀경우  시간, 분등이 바뀜 =========
hour    = 17
minute  = 44
link    = "https://www.youtube.com/watch?v=dcOwj-QE_ZE"
# =================================================================

# ========== 전역 저장전에 삽입할 템프 =========
temp_hour    = 17
temp_minute  = 44
temp_link    = "https://www.youtube.com/watch?v=dcOwj-QE_ZE"
# =================================================================
    

class CWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.year = QLCDNumber(self)
        self.month = QLCDNumber(self)
        self.day = QLCDNumber(self)
        self.hour = QLCDNumber(self)
        self.min = QLCDNumber(self)
        self.sec = QLCDNumber(self)
        self.editText = QLineEdit()
        self.applyBtn = QPushButton()
        self.applyBtn.setText("적용하기")
        self.applyBtn.clicked.connect(self.applyBtn_event)
       
    


        self.comboBoxHour = QComboBox(self)
        for hour in range(24):
            strHours = str(hour) + "시"
            self.comboBoxHour.addItem(strHours)
        
        self.comboBoxMinute = QComboBox(self)
        for minute in range(60):
            strMinute = str(minute) + "분"
            self.comboBoxMinute.addItem(strMinute)
     
        self.comboBoxHour.activated[str].connect(self.onActivated)
        self.comboBoxMinute.activated[str].connect(self.onActivated)

        

        # LCD 글자색 변경
        pal = QPalette()
        pal.setColor(QPalette.WindowText, QColor(255,0,0))
        self.sec.setPalette(pal)

        # # LCD 배경색 변경
        # pal = QPalette()
        # pal.setColor(QPalette.Background, QColor(255,0,0))
        # self.min.setPalette(pal)
        # self.min.setAutoFillBackground(True)

        self.initUI()

    def initUI(self):
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.year)
        hbox1.addWidget(self.month)
        hbox1.addWidget(self.day)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.hour)
        hbox2.addWidget(self.min)
        hbox2.addWidget(self.sec)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.comboBoxHour)
        hbox3.addWidget(self.comboBoxMinute)

        hbox4 = QGridLayout()
        hbox4.addWidget(self.editText)
        hbox4.addWidget(self.applyBtn)
        


        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)


        

        self.setLayout(vbox)

        self.setWindowTitle('side Project')
        self.setGeometry(300, 200, 400, 200)

        self.showtime()

    def showtime(self):
        global macro
        # 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과시간 (초단위)
        t = time.time()
        # 한국 시간 얻기
        kor = time.localtime(t)
        # LCD 표시
        self.year.display(kor.tm_year)
        self.month.display(kor.tm_mon)
        self.day.display(kor.tm_mday)
        self.hour.display(kor.tm_hour)
        self.min.display(kor.tm_min)
        self.sec.display(kor.tm_sec)

        # 특정 시간에 매크로 시작
        if kor.tm_hour == hour and kor.tm_min == minute:
            if macro == True :
                pyautogui.typewrite(["WIN"])
                time.sleep(0.5)
                pyautogui.typewrite('Chrome')
                time.sleep(0.5)
                pyautogui.typewrite(['enter'])
                time.sleep(0.5)
                #pyautogui.typewrite("https://youtu.be/3iM_06QeZi8")
                clipboard.copy(link)
                pyautogui.hotkey("ctrl", "V")
                time.sleep(0.5)
                pyautogui.typewrite(["enter"])
                time.sleep(0.5)
                pyautogui.typewrite(["F11"])
                time.sleep(0.5)
                pyautogui.typewrite(["f"])

                macro = False

        # 자정에 매크로 초기화
        if kor.tm_hour == 0 and kor.tm_min == 0 and kor.tm_hour == 0 and kor.tm_sec == 0 :
            macro = True


        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()


    def onActivated(self, text):
        temp = ""
        for char in range(len(text)-1):
            if type(text[char]) != "<class 'str'>" :
                temp+= text[char]
                
        if text[len(text)-1] == "분":
            global temp_minute
            temp_minute = int(temp)
        if text[len(text)-1] == "시":
            global temp_hour
            temp_hour = int(temp)

    def applyBtn_event(self):
        global link
        link = self.editText.text()
        
        global temp_hour
        global temp_minute

        global hour
        global minute

        hour = temp_hour
        minute = temp_minute
        print(link)
        print(temp_hour)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())