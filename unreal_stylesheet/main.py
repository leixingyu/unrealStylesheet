import os
from contextlib import suppress


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
QSS_PATH = os.path.join(MODULE_PATH, 'ue.qss')
ICONS_RCC = os.path.join(MODULE_PATH, 'icons.rcc')


def import_qt_bindings():
    """
    Import the active Qt Bindings based on the active QApplication.
    This prevents importing the wrong Qt bindings, 
    if the user has multiple Qt bindings installed
    """
    active_qapp = None
    QtWidgets = None
    QtCore = None
    if not active_qapp:
        with suppress(ImportError):
            from PySide6 import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
    if not active_qapp:
        with suppress(ImportError):
            from PyQt6 import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
    if not active_qapp:
        with suppress(ImportError):
            from PySide2 import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
            print (active_qapp)
    if not active_qapp:
        with suppress(ImportError):
            from PyQt5 import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
    if not active_qapp:
        with suppress(ImportError):
            from PySide import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
    if not active_qapp:
        with suppress(ImportError):
            from PyQt4 import QtWidgets, QtCore
            active_qapp = QtWidgets.QApplication.instance()
        
    # add them to global
    globals()['QtWidgets'] = QtWidgets
    globals()['QtCore'] = QtCore


def setup():
    """
    Apply the Unreal dark stylesheet to the current QApplication
    """
    import_qt_bindings()

    try:
        # for PyQt5 & PySide2
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    except AttributeError:
        # enabled by default in PyQt6 & PySide6
        pass

    app = QtWidgets.QApplication.instance()
    QtCore.QResource.registerResource(ICONS_RCC)
    with open(QSS_PATH, 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)
