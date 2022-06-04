import sys
import os

from Qt import QtWidgets, QtCore, QtGui
from Qt import _loadUi


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
UI_PATH = os.path.join(MODULE_PATH, 'ui', 'progress.ui')
QSS_PATH = os.path.join(MODULE_PATH, 'ue.qss')


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)

    QtCore.QResource.registerResource("icons.rcc")

    with open(QSS_PATH, 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)

    window = QtWidgets.QMainWindow()
    _loadUi(UI_PATH, window)
    window.show()

    sys.exit(app.exec_())
