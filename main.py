# ch 4.2.1 main.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)  # QMessageBos : 메세지박스 위젯
from PyQt5.QtGui import QIcon   # icon 추가하기 위한 라이브러리
class Calculator(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.btn1=QPushButton('Message', self)  # 버튼추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        vbox=QVBoxLayout()  # 수직 레이앗웃 위젯 생성
        vbox.addStretch(1)  # 빈공간
        vbox.addWidget(self.btn1)   # 버튼위치
        vbox.addStretch(1)  # 빈공간

        self.setLayout(vbox)    # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon-1.jfif'))    # 윈도 아이콘 추가
        self.resize(256,256)
        self.show()

    def activateMessage(self) :    # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        QMessageBox.information(self, "information", "Button Clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())