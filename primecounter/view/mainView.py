from PySide.QtGui import QMainWindow, QMessageBox, QListWidgetItem
from PySide.QtCore import QThread, Signal
from view.gen.mainView import Ui_MainWindow
import logging

import threading

loggerReport = logging.getLogger(__name__ + ".Report")

WINDOW_TITLE = 'Accenture Prime Counter'


class MainView(QMainWindow, Ui_MainWindow):

    LOWER_LIMIT = 2

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi()
        self.workThread = None

    def setupUi(self):
        super().setupUi(self)
        self.setWindowTitle(WINDOW_TITLE)
        self.setupConnections()

    def setupConnections(self):
        self.searchButton.clicked.connect(self.onSearch)

    def onSearch(self):

        try:
            limit = int(self.tleLimit.text().strip())
        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Ongeldige limiet')
            msgBox.setText('Vul een geldige limiet in')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()
            return

        if limit < self.LOWER_LIMIT:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Ongeldige limiet')
            msgBox.setText('Vul een geldige limiet in')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()
            return

        if self.rbAKS.isChecked():
            algorithm = aks
        elif self.rbML.isChecked():
            algorithm = aks

        self.search(algorithm, limit)

    def search(self, algorithm, limit):

        self.resetResults()
        self.workThread = ComputePrimeThread(algorithm, limit)
        self.workThread.onResult.connect(self.wrapup)
        self.workThread.start()
        self.interruptButton.clicked.connect(self.workThread.stop)
        self.interruptButton.setEnabled(True)

    def wrapup(self, result):

        self.interruptButton.setEnabled(False)
        self.showResult(result)

    def showResult(self, result):

        self.tleResultCount.setText(str(len(result)))

        for prime in result:
            item = QListWidgetItem(str(prime))
            self.listResults.addItem(item)

    def resetResults(self):

        self.tleResultCount.setText(None)
        self.listResults.clear()


class ComputePrimeThread (QThread):

    onResult = Signal(list)

    def __init__(self, runnable, n):
        QThread.__init__(self)

        self.runnable = runnable
        self.n = n
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):

        res = []

        for i in range(2, self.n + 1):

            if self.stopped():
                break

            if self.runnable(i):
                res.append(i)

        self.onResult.emit(res)


def expand_x_1(n):
    # This version uses a generator and thus less computations
    c = 1
    for i in range(n // 2 + 1):
        c = c * (n - i) // (i + 1)
        yield c


def aks(p):
    if p == 2:
        return True

    for i in expand_x_1(p):
        if i % p:
            # we stop without computing all possible solutions
            return False
    return True
