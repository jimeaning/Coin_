import sys
import time

from PyQt5.QtGui import QBrush, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import ccxt

#ui
form_class = uic.loadUiType("CoinUi.ui")[0]

#api
binance = ccxt.binance({
    'apiKey' : 'HDOOTS8GppfdMzUrLGfw9ZZFvjJDB2Z8bhIa5Zix2dIvwgbmJPIsHGSAuUWDoie4',
    'secret' : 'CU48p99aBAiDo9sbpdzcE8scSINa2gFmePEhM15zp1iQIJtxPu9CDzi0HU4MAX64',
})

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('코인 거래 프로그램')
        self.setWindowIcon(QIcon("icon.png"))

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

        self.Qprice.textChanged.connect(self.lineeditTextFunction)

        # 현재가 조회
        self.inquiry_btn.clicked.connect(self.inquiry)

        self.show()


    def initUi(self):
        buy_btn = QPushButton("매수", self)
        buy_btn.clicked.connect(self.buy_btn_clicked) # 클릭 시 실행할 function

        sell_btn = QPushButton("매도", self)
        sell_btn.clicked.connect(self.sell_btn_clicked)

        buy_cancel_btn = QPushButton("취소", self)
        buy_cancel_btn.clicked.connect(self.buy_cancel_btn_clicked)

        sell_cancel_btn = QPushButton("취소", self)
        sell_cancel_btn.clicked.connect(self.sell_cancel_btn_clicked)

        buy_end_btn = QPushButton("청산", self)
        buy_end_btn.clicked.connect(self.buy_end_btn_clicked)

        sell_end_btn = QPushButton("청산", self)
        sell_end_btn.clicked.connect(self.sell_end_btn_clicked)


    def lineeditTextFunction(self):
        self.Qprice.setText(self.Qprice.text())


    # 지정가 매수
    def buy_btn_clicked(self):
        data = float(self.Qprice.text())
        order = binance.create_limit_buy_order('ETH/BTC', 50, data)
        print(order)
        resp = binance.fetch_order(74813964, 'ETH/BTC')
        print(resp)

    # 매수 취소
    def buy_cancel_btn_clicked(self):
        resp = binance.cancel_order(74813964, "XRP/BNB")
        print(resp)

    # 지정가 매도
    def sell_btn_clicked(self):
        data = float(self.Qprice.text())
        order = binance.create_market_sell_order('ETH/BTC', 50, data)
        print(order)
        resp = binance.fetch_order(74813964, 'ETH/BTC')
        print(resp)

    # 현재가 조회
    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("현재 시간 hh:mm:ss")
        self.statusBar().showMessage(str_time)

        price = binance.fetch_ticker('ETH/BTC')
        self.label.setText("비트코인 현재가: " + str(price['close']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

