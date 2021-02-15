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
    'apiKey' : 'zQ73OitWm4NVUVTsFsaFn2hr5pXpR97goV8fY98AcA8Sd1cGulAlnZIah2ld1EyE',
    'secret' : '4Ztwf0iqU5sYdxcqMTvfKjBNYQehzboxufe1SwtWHrYXSuqcLvDT3K1F5UmUFXyd',
})

balance = binance.fetch_balance()
print(balance['ETH']['free'], balance['ETH']['used'], balance['ETH']['total'])

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.setWindowTitle('코인 거래 프로그램')
        self.setWindowIcon(QIcon("icon.png"))

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

        self.show()


    def initUi(self):
        # 현재가 조회
        self.inquiry_btn.clicked.connect(self.inquiry)
        # 매수
        self.buy_btn.clicked.connect(self.buy_btn_clicked)
        # 매도
        self.sell_btn.clicked.connect(self.sell_btn_clicked)

        #self.Qprice.textChanged.connect(self.lineeditTextFunction)
        #self.Qamount.textChanged.connect(self.lineeditTextFunction)

    #def lineeditTextFunction(self):
        #self.price_la.setText(self.price_data.text)


    # 지정가 매수
    def buy_btn_clicked(self):
        order = binance.create_limit_buy_order('BTC/BUSD', self.Qamount.text(), self.Qprice.text())
        print(order)
        self.Qprice.clear()
        self.Qamount.clear()

    # 매수 취소
    def buy_cancel_btn_clicked(self):
        resp = binance.cancel_order(74813964, "XRP/BNB")
        print(resp)

    # 지정가 매도
    def sell_btn_clicked(self):
        order = binance.create_limit_sell_order('BTC/BUSD', self.Qamount.text(), self.Qprice.text())
        print(order)
        #resp = binance.fetch_order(1272630444, 'ETH/BUSD')
        #print(resp)
        self.Qprice.clear()
        self.Qamount.clear()

    # 현재가 조회랑 현재 시간
    def inquiry(self):
        price = binance.fetch_ticker("ETH/BTC")
        self.label.setText("현재가: " + str(price['close']))

        cur_time = QTime.currentTime()
        str_time = cur_time.toString("현재 시간 hh:mm:ss")
        self.statusBar().showMessage(str_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

