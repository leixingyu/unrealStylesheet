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


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
QSS_PATH = os.path.join(MODULE_PATH, 'ue.qss')
ICONS_RCC = os.path.join(MODULE_PATH, 'icons.rcc')


def setup():
    """
    Apply the Unreal dark stylesheet to the current QApplication
    """
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication.instance()
    QtCore.QResource.registerResource(ICONS_RCC)
    with open(QSS_PATH, 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)
