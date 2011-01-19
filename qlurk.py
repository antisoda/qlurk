#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class qlurk(object):
  def __init__(self):
    self.window = QMainWindow()
    self.widget = QWidget()
    self.window.setCentralWidget(self.widget)

    layout = QVBoxLayout(self.widget)

    self.web = QWebView(self.widget)
    self.web.load(QUrl("http://plurk.com/m"))
    layout.addWidget(self.web)
    self.window.resize(320, 500)
    self.window.show()
    self.window.setWindowTitle("qlurk")

app = QApplication(sys.argv)
plurk = qlurk()
sys.exit(app.exec_())

