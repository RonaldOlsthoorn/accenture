import sys
import os
import logging
import logging.config
from PySide import QtGui
from view.mainView import MainView
import signal


class PrimeCounter(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(PrimeCounter, self).__init__(sys_argv)

        self.mainView = MainView()

        if os.name == 'nt':
            # This is needed to display the app icon on the taskbar on Windows
            # 7
            import ctypes
            myappid = 'Accenture.Primecounter'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                myappid)


if __name__ == '__main__':

    # Enable ctrl-c closeable
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = PrimeCounter(sys.argv)

    # Center the application
    screenGeometry = app.desktop().screenGeometry()
    x = (screenGeometry.width() - app.mainView.width()) / 2
    y = (screenGeometry.height() - app.mainView.height()) / 2
    app.mainView.move(x, y)
    app.mainView.show()

    sys.exit(app.exec_())
