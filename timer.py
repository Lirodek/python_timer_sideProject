### intro.
## Date : 2020. 11. 26
## Editer : 성원경 선생님 / 경기기계공업고등학교

### 3. 유튜브 매크로 알람 시계

<<<<<<< Updated upstream
### 디지털 시계 코드
# 배광민 첫번째 주석 1 
=======
### 디지털 시계 코드 
from calendar import week
>>>>>>> Stashed changes
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

class CWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.year = QLCDNumber(self)
        self.month = QLCDNumber(self)
        self.day = QLCDNumber(self)
        self.hour = QLCDNumber(self)
        self.min = QLCDNumber(self)
        self.sec = QLCDNumber(self)


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


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setWindowTitle('원킹의 유튜브 알람 시계')
        self.setGeometry(200, 200, 400, 200)

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
        if kor.tm_hour == 15 and kor.tm_min == 27:
            if macro == True :
                pyautogui.typewrite(["WIN"])
                time.sleep(0.5)
                pyautogui.typewrite('Chrome')
                time.sleep(0.5)
                pyautogui.typewrite(['enter'])
                time.sleep(0.5)
                #pyautogui.typewrite("https://youtu.be/3iM_06QeZi8")
                clipboard.copy("https://youtu.be/3iM_06QeZi8")
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
            self.updateData()
<<<<<<< Updated upstream
            macro = True

=======
        # testHour = 12
        # testMinute = 46
        # if kor.tm_hour == testHour and kor.tm_min == testMinute and kor.tm_hour == testHour and kor.tm_sec == 0 :
        #     print("이거 실행됐어")
        #     self.updateData()
>>>>>>> Stashed changes

        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()

<<<<<<< Updated upstream
=======
    def updateData(self):
        global hour, minute, link
        result = self.rows( daillyDay[ datetime.today().weekday() ])
        if len(result) == 0 :
            QMessageBox. question(self, '확인창', '알람설정하시겠어요?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        for tuple in result:
            hour = tuple[0]
            minute = tuple[1]
            link = tuple[2]
            print(tuple[0])
            

    # 시, 분을 가져오는 함수
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

    # 요일 버튼을 리셋해주는 함수
    def weekButtonReset(self):
        i = 0
        for day in self.days:
            day.setStyleSheet(defaultButtonString)
            week_hover[i] = 0
            i+=1

    def applyBtn_event(self):
        global temp_hour
        global temp_minute
        global hour
        global minute
        global macro
        global link

        reply = QMessageBox.question(self, '확인창', '알람설정하시겠어요?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            macro = True
            self.weekButtonReset()

            if self.editText.text() != "":
                link = self.editText.text()

            print('알람 저장되어야할 값들', temp_hour,'시', temp_minute, week_hover)
            hour = temp_hour
            minute = temp_minute

        else:
            print('취소되었습니다.')
>>>>>>> Stashed changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())