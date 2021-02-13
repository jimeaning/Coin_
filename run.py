import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ccxt

binance = ccxt.binance()
binance.apiKey = 'HDOOTS8GppfdMzUrLGfw9ZZFvjJDB2Z8bhIa5Zix2dIvwgbmJPIsHGSAuUWDoie4'
binance.secret = 'CU48p99aBAiDo9sbpdzcE8scSINa2gFmePEhM15zp1iQIJtxPu9CDzi0HU4MAX64'

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 800, 500)
        self.setWindowTitle("코인 거래 프로그램")
        self.setWindowIcon(QIcon("icon.png"))

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        buy_btn = QPushButton("매수", self)
        buy_btn.move(100, 50)
        cancel_btn = QPushButton("취소", self)
        cancel_btn.move(210, 50)
        end_btn = QPushButton("청산", self)
        end_btn.move(320, 50)

        buy_btn2 = QPushButton("매도", self)
        buy_btn2.move(100, 90)
        cancel_btn2 = QPushButton("취소", self)
        cancel_btn2.move(210, 90)
        end_btn2 = QPushButton("청산", self)
        end_btn2.move(320, 90)

        buy_btn.clicked.connect(self.buy_btn_clicked)

    def buy_btn_clicked(self):
        order = binance.create_limit_buy_order('XRP/BNB', 50, 0.03)
        print(order)
        resp = binance.fetch_order(74813964, "XRP/BNB")
        print(resp)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)


app= QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()