import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time
import pyautogui
import clipboard

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab = QTabWidget()

        tab_1 = self.create_tab_1()
        tab_2 = self.create_tab_2()

        tab.addTab(tab_1, "tab_1")
        tab.addTab(tab_2, "tab_2")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab)

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()

    def create_tab_1(self):
        formlayout = QFormLayout()
        name = QLineEdit()
        age = QSpinBox()
        formlayout.addRow("Name", name)
        formlayout.addRow("Age", age)
        for index in range(100):
            formlayout.addRow("button_{}".format(index), QPushButton(str(index)))

        widget = QWidget()
        widget.setLayout(formlayout)
        #scroll_area = QScrollArea()
        #scroll_area.setWidget(widget)
        #scroll_area.setWidgetResizable(True)
        return widget

    def create_tab_2(self):
        layout = QVBoxLayout()
        button = QPushButton("Button")
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        return scroll_area

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())