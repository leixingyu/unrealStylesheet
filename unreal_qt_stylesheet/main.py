# import sys
import os


try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    pass

try:
    from PyQt5 import QtWidgets, QtCore, QtGui
except ImportError:
    pass

try:
    from PySide6 import QtWidgets, QtCore, QtGui
except ImportError:
    pass

try:
    from PyQt6 import QtWidgets, QtCore, QtGui
except ImportError:
    pass

# from Qt import QtWidgets, QtCore, QtGui
# from Qt import _loadUi
from pathlib import Path


# MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
# UI_PATH = os.path.join(MODULE_PATH, 'ui', 'progress.ui')
# QSS_PATH = os.path.join(MODULE_PATH, 'ue.qss')
MODULE_PATH = Path(os.path.abspath(__file__)).parent
QSS_PATH = MODULE_PATH / 'ue.qss'


def setup():
    """ Apply the Unreal dark stylesheet to the current QApplication """
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication.instance()
    QtCore.QResource.registerResource(str(MODULE_PATH / "icons.rcc") )
    with open(QSS_PATH, 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)


# if __name__ == '__main__':
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     app = QtWidgets.QApplication(sys.argv)
#
#     QtCore.QResource.registerResource("icons.rcc")
#
#     with open(QSS_PATH, 'r') as f:
#         qss = f.read()
#         app.setStyleSheet(qss)
#
#     window = QtWidgets.QMainWindow()
#     _loadUi(UI_PATH, window)
#     window.show()
#
#     sys.exit(app.exec_())
