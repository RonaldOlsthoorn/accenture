from PySide.QtGui import *
from PySide.QtCore import *
from view.gen.mainView import Ui_MainWindow

import logging

loggerReport = logging.getLogger(__name__ + ".Report")

WINDOW_TITLE = 'Accenture Prime Counter'


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        self.setWindowTitle(WINDOW_TITLE)
        self.setupConnections()

    def setupConnections(self):
        self.searchButton.clicked.connect(self.search)

    def search(self):
        print("something")
