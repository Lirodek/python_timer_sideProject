### intro.
## Date : 2020. 11. 26
## Editer : 배광민 위피아/주임

### 3. 유튜브 매크로 알람 시계 개선

### 디지털 시계 코드 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import pythonDB
import time
import pyautogui
import clipboard
from datetime import datetime



QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

macro = True
# ========== 전역 변수 이 값을 바꿀경우  시간, 분등이 바뀜 =========
hour    = 17
minute  = 10
link    = "https://www.youtube.com/watch?v=Y8JFxS1HlDo"
# =================================================================

# =================== 전역 저장전에 삽입할 템프 ===================
temp_hour    = 17
temp_minute  = 44
temp_link    = "https://www.youtube.com/watch?v=dcOwj-QE_ZE"
# =================================================================

# =========== default and hover button style ==========
#            and week in day Select ? ( 0 ? no : yes ) 
defaultButtonString = "color: black;font-size : 15px;border-style: solid;border-width: 1px;border-color: #000000;border-radius: 1px;"
hoverButtonString = "color: black;font-size : 15px;background-color: gray;border-style: solid;border-width: 1px;border-color: #000000;border-radius: 1px;"
week_hover = [0, 0, 0, 0, 0, 0, 0]
daillyDay = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# =====================================================

# =========== select Day variable ===========
selectDate =''
SelectDayData = []
selectLoofData = []
# =====================================================

# labelClickEvent
def clickable(widget, text):

    class Filter(QObject):
        #pyside2 사용자는 pyqtSignal() -> Signal()로 변경
        clicked = pyqtSignal()	

        def eventFilter(self, obj, event):
            
            # Is the object receiving the click event a widget?
            # 클릭 이밴트를 받은 객체가 위젯인가요?
            if obj == widget:

                # event type is MouseButtonRelease ?
                # 이밴트의 유형이 마우스 클릭인가요?
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        i = 0
                        for day in text.days:
                            if day == widget:
                                global week_hover
                                if week_hover[i] == 0:
                                    week_hover[i] = 1
                                    print(week_hover)
                                    widget.setStyleSheet(hoverButtonString)
                                else:
                                    week_hover[i] = 0
                                    widget.setStyleSheet(defaultButtonString)
                                print(i)
                            i+=1

                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

# 위젯 실행시 호출되는 클래스
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
        self.database = pythonDB
        self.rows = self.database.test
        self.updateData()   

        # weekButton Setting 일 ~ 월
        self.days = [QLabel('일'),QLabel('월'),QLabel('화'),QLabel('수'),QLabel('목'),QLabel('금'),QLabel('토'),]
        for i in range(7):
            self.days[i].setStyleSheet(defaultButtonString)
            clickable(self.days[i], self).connect(self.pressEvent)
        
        # 관리 => 삭제버튼
        self.deleteBtn = QPushButton()
        self.deleteBtn.setText("삭제")
       
        # selectBox 0시~23시
        self.comboBoxHour = QComboBox(self)
        for hour in range(24):
            strHours = str(hour) + "시"
            self.comboBoxHour.addItem(strHours)
        
        # selectBox 0분~59분
        self.comboBoxMinute = QComboBox(self)
        for minute in range(60):
            strMinute = str(minute) + "분"
            self.comboBoxMinute.addItem(strMinute)

        # ========= select Days =========
        # selectBox 0시~23시
        self.comboBoxHourSelectDay = QComboBox(self)
        for hour in range(24):
            strHours = str(hour) + "시"
            self.comboBoxHourSelectDay.addItem(strHours)
        
        # selectBox 0분~59분
        self.comboBoxMinuteSelectDay = QComboBox(self)
        for minute in range(60):
            strMinute = str(minute) + "분"
            self.comboBoxMinuteSelectDay.addItem(strMinute)
        
        self.editTextSelectDay = QLineEdit()
        self.applyBtnSelectDay = QPushButton()

        self.applyBtnSelectDay.setText("적용하기")
        self.applyBtnSelectDay.clicked.connect(self.applyBtn_eventSelectDay)

        self.comboBoxHour.activated[str].connect(self.onActivated)
        self.comboBoxMinute.activated[str].connect(self.onActivated)

        self.comboBoxHourSelectDay.activated[str].connect(self.onActivated)
        self.comboBoxMinuteSelectDay.activated[str].connect(self.onActivated)

        

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

    # 전체적인 ui 설정 탭넣으려면 여기서넣으면됨.
    def initUI(self):
        tab = QTabWidget()

        tab_1 = self.create_tab_1()
        tab_2 = self.create_tab_2()
        tab_3 = self.create_tab_3()

        tab.addTab(tab_1, "반복 알람")
        tab.addTab(tab_2, "날짜 알람")
        tab.addTab(tab_3, "알람 관리")
    
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab)

        self.setLayout(main_layout)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('timerIcon.jpeg'))
        self.setWindowTitle('timer')
        self.setGeometry(300, 400, 300, 250)

        self.showtime()

    # 첫번째 탭
    def create_tab_1(self):
        widget = QWidget()
        
        # QLED 연 월 일
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.year)
        hbox1.addWidget(self.month)
        hbox1.addWidget(self.day)
        
        # QLED 시 분 초
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.hour)
        hbox2.addWidget(self.min)
        hbox2.addWidget(self.sec)

        # SelectBox  시 분
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.comboBoxHour)
        hbox3.addWidget(self.comboBoxMinute)

        #유튜브 링크 click
        hbox4 = QGridLayout()
        hbox4.addWidget(self.editText)
        hbox4.addWidget(self.applyBtn)
        
        # Week Button
        hbox6 = QHBoxLayout()
        for i in range(7):
            hbox6.addWidget(self.days[i])



        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        # vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        widget.setLayout(vbox)

        return widget
    
    # 캘린더 클릭시 현재 셀렉한 날짜
    def showDate(self, date):
        global selectDate
        selectDate = date.toString("yyyyMMdd")

    # 첫번째 탭
    def pressEvent(self):
        self.days

    # 두번째 탭 
    def create_tab_2(self):
        widget = QWidget()

        # hbox1 = QHBoxLayout()
        # textBrowser = QTextBrowser()
        # textBrowser.setAcceptRichText(True)
        # textBrowser .setOpenExternalLinks(True)
        # hbox1.addWidget(textBrowser)

        
        hbox1 = QHBoxLayout()
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        hbox1.addWidget(cal)

        # SelectBox  시 분
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.comboBoxHourSelectDay)
        hbox3.addWidget(self.comboBoxMinuteSelectDay)

        #유튜브 링크 click
        hbox4 = QGridLayout()
        hbox4.addWidget(self.editTextSelectDay)
        hbox4.addWidget(self.applyBtnSelectDay)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        # vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        widget.setLayout(vbox)

        return widget
    # 세번째 탭
    def create_tab_3(self):
        widget = QWidget()

        # hbox1 = self.changeSelectDayTable()

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.deleteBtn)

        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox2)

        widget.setLayout(vbox)

        return widget

    # 1초마다 실행시켜주는 함수
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
                clipboard.copy("Chrome")
                pyautogui.hotkey("ctrl", "V")
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
                self.updateData()

        # 자정에 매크로 초기화
        if kor.tm_hour == 0 and kor.tm_min == 0 and kor.tm_hour == 0 and kor.tm_sec == 0 :
            self.update()

        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()

    # 데이터베이스에서 가장 최근의 설정한 시간과 분을 가져오는 함수
    def updateData(self):
        global hour, minute, link
        global macro
        result = self.rows( daillyDay[ datetime.today().weekday() ])
        # if len(result) == 0 :
        #     QMessageBox. question(self, '확인창', '저장된 알람이 없습니다.')

        for tuple in result:
            hour = tuple[0]
            minute = tuple[1]
            link = tuple[2]
            macro = True
            print(str(type(hour))+'시'+str(minute)+'분'+str(macro))
            
            

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
        print(str(temp_hour)+","+str(temp_minute))

    # 요일 버튼을 리셋해주는 함수
    def weekButtonReset(self):
        i = 0
        for day in self.days:
            day.setStyleSheet(defaultButtonString)
            week_hover[i] = 0
            i+=1

    # 테이블박스를 생성해주는 함수.
    # def changeSelectDayTable(self):
    #     global SelectDayData
    #     row = self.database.selectDayCount()
    #     self.table = QTableWidget(row[0][0], 5, self)  # row, column
    #     self.table.setHorizontalHeaderLabels(["", "DATE", "HOUR",  "MINUTE", "LINK"])
    #     SelectDayData = self.database.selectDayTimer()
    #     for idx, (key_num, date, hour, minute, lnk) in enumerate(SelectDayData):
    #         # 사용자정의 item 과 checkbox widget 을, 동일한 cell 에 넣어서 , 추후 정렬 가능하게 한다.
    #         item = MyQTableWidgetItemCheckBox()
    #         self.table.setItem(idx, 0, item)
    #         chbox = MyCheckBox(item)
    #         # print(chbox.sizeHint())
    #         self.table.setCellWidget(idx, 0, chbox)

    #         chbox.stateChanged.connect(self.__checkbox_change)  # sender() 확인용 예..

    #         self.table.setItem(idx, 0, QTableWidgetItem(key_num))
    #         self.table.setItem(idx, 1, QTableWidgetItem(date))
            
    #         # 숫자를 기준으로 정렬하기 위함. -- default 는 '문자'임.
    #         item = QTableWidgetItem()
    #         item.setData(Qt.DisplayRole, hour)
    #         self.table.setItem(idx, 2, item)

    #         item2 = QTableWidgetItem()
    #         item2.setData(Qt.DisplayRole, minute)
    #         self.table.setItem(idx, 3, item2)
    #         self.table.setItem(idx, 4, QTableWidgetItem(lnk))

    #         self.table.setSortingEnabled(False)  # 정렬기능
    #     self.table.resizeRowsToContents()
    #     self.table.resizeColumnsToContents()  # 이것만으로는 checkbox 컬럼은 잘 조절안됨.
    #     self.table.setColumnWidth(0, 15)  # checkbox 컬럼 폭 강제 조절.

    #     self.table.cellClicked.connect(self._cellclicked)

    #     # 컬럼 헤더를 click 시에만 정렬하기.
    #     hheader = self.table.horizontalHeader()  # qtablewidget --> qtableview --> horizontalHeader() --> QHeaderView
    #     hheader.sectionClicked.connect(self._horizontal_header_clicked)
    #     vbox = QHBoxLayout(self)
    #     vbox.addWidget(self.table)
    #     return vbox
        # 여기까지 했음. 22.10.17

    def _horizontal_header_clicked(self, idx):
        """
        컬럼 헤더 click 시에만, 정렬하고, 다시 정렬기능 off 시킴
         -- 정렬기능 on 시켜놓으면, 값 바뀌면 바로 자동으로 data 순서 정렬되어 바뀌어 헷갈린다..
        :param idx -->  horizontalheader index; 0, 1, 2,...
        :return:
        """
        # print("hedder2.. ", idx)
        self.table.setSortingEnabled(True)  # 정렬기능 on
        # time.sleep(0.2)
        self.table.setSortingEnabled(False)  # 정렬기능 off

    
    def _cellclicked(self, row, col):
        print(SelectDayData[row])
        print("_cellclicked... ", row, col)


    # 버튼 설정버튼 클릭시 동작하는 함수.
    def applyBtn_event(self):
        global temp_hour
        global temp_minute
        global macro
        global temp_link
        global week_hover
        select_day_ofTheWeek = False

        reply = QMessageBox.question(self, '확인창', '알람설정하시겠어요?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            macro = True
           

            if self.editText.text() != "":
                temp_link = self.editText.text()
            
            for i in range(7):
                if(week_hover[i]==1):
                    print('요일체크함.')
                    select_day_ofTheWeek=True
            
            if(select_day_ofTheWeek):
                insertText = "('lirodek',"+str(temp_hour)+","+str(temp_minute)+","+"'"+str(temp_link)+"'"+","+str(week_hover[0])+","+str(week_hover[1])+","+str(week_hover[2])+","+str(week_hover[3])+","+str(week_hover[4])+","+str(week_hover[5])+","+str(week_hover[6])+")"
                self.database.insertLoof(insertText)
            else:
                insertText = "('lirodek', DATE_FORMAT(now(), '%Y%m%d'),"+str(temp_hour)+","+str(temp_minute)+","+"'"+str(temp_link)+"')"
                self.database.insertToDayTimer(insertText)

            # insrt시 에러나면 이위치에 로그 찍으셈 0 오류 1 통과
           
            self.updateData()
            self.weekButtonReset()

        else:
            print('취소되었습니다.')

    
    # def __checkbox_change(self, checkvalue):
    #     # print("check change... ", checkvalue)
    #     chbox = self.sender()  # signal을 보낸 MyCheckBox instance
    #     print("checkbox sender row = ", chbox.get_row())

    def applyBtn_eventSelectDay(self):
        print('입장')
        global temp_hour
        global temp_minute
        global macro
        global temp_link

        reply = QMessageBox.question(self, '확인창', '알람설정하시겠어요?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            macro = True
           
            if self.editText.text() != "":
                temp_link = self.editTextSelectDay.text()

            insertText = "('lirodek', "+str(selectDate)+","+str(temp_hour)+","+str(temp_minute)+","+"'"+str(temp_link)+"')"
            self.database.insertToDayTimer(insertText)

            # insrt시 에러나면 이위치에 로그 찍으셈 0 오류 1 통과
            self.updateData()
            self.weekButtonReset()

        else:
            print('취소되었습니다.')
# class MyCheckBox(QCheckBox):
#     def __init__(self, item):
#         """
#         :param item: QTableWidgetItem instance
#         """
#         super().__init__()
#         self.item = item
#         self.mycheckvalue = 0   # 0 --> unchecked, 2 --> checked
#         self.stateChanged.connect(self.__checkbox_change)
#         self.stateChanged.connect(self.item.my_setdata)  # checked 여부로 정렬을 하기위한 data 저장

#     def __checkbox_change(self, checkvalue):
#         # print("myclass...check change... ", checkvalue)
#         self.mycheckvalue = checkvalue
#         print("checkbox row= ", self.get_row())

#     def get_row(self):
#         return self.item.row()
# class MyQTableWidgetItemCheckBox(QTableWidgetItem):
#     """
#     checkbox widget 과 같은 cell 에  item 으로 들어감.
#     checkbox 값 변화에 따라, 사용자정의 data를 기준으로 정렬 기능 구현함.
#     """
#     def __init__(self):
#         super().__init__()
#         self.setData(Qt.UserRole, 0)

#     def __lt__(self, other):
#         # print(type(self.data(Qt.UserRole)))
#         return self.data(Qt.UserRole) < other.data(Qt.UserRole)

#     def my_setdata(self, value):
#         # print("my setdata ", value)
#         self.setData(Qt.UserRole, value)
#         # print("row ", self.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())