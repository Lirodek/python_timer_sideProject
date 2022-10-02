import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class comboBoxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lb1 = QLabel('선택하세요.', self)
        self.lb1.move(10,20)

        combo_box = QComboBox(self)
        for sec in range(24):
            strSecond = str(sec) + "시"
            combo_box.addItem(strSecond)
            combo_box.move(100,15)
            combo_box.activated[str].connect(self.onActived)

        self.setWindowTitle('콤보박스')
        self.setGeometry(500,500,200,100)
        self.show()

    def onActived(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = comboBoxApp()
    sys.exit(app.exec_())