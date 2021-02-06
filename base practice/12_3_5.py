import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        # dynamicCall 원하는 메서드 호출
        # Open API+가 제공하는 메서드를 사용하려면 self.kiwoom 객체를 통해 dynamicCall 메서드를 호출해야 합니다.
        # 이때 dynamicCall 메서드의 인자로 호출하려는 메서드를 전달합니다.
        self.setWindowTitle("종목 코드")
        self.setGeometry(300, 300, 300, 150)

        btn1 = QPushButton("종목코드 얻기", self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 170, 130)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        # 장내 주식 종목코드
        kospi_code_list = ret.split(';')
        # 종목코드 리스트, 종목간 구분은 ';'
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            # GetMasterCodeName 해당 종목코드의 한글명 반환
            kospi_code_name_list.append(x + " : " + name)
            # 코드명 : 종목이름

        self.listWidget.addItems(kospi_code_name_list)
        # 종목 코드와 한글 종목명이 저장된 파이썬 리스트를 addItems 메서드의 인자로 전달해서
        # 파이썬 리스트에 있는 항목을 QListWidget에 추가.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())



