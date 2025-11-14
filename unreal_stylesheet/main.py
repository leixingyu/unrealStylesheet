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


def setup(app=None):
    """
    Apply the Unreal dark stylesheet to the current QApplication
    """
    import_qt_bindings()

    # Enable High Dpi Scaling only in Qt5 (PyQt5, PySide2, etc.)
    # In Qt6 (PyQt6, PySide6), this is enabled by default and the attribute is deprecated
    qt_version = QtCore.qVersion()
    if int(qt_version.split('.')[0]) < 6:
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = app or QtWidgets.QApplication.instance()
    QtCore.QResource.registerResource(ICONS_RCC)
    with open(QSS_PATH, 'r') as f:
        qss = f.read()
        app.setStyle("Fusion")  # dark title bar in Qt6
        app.setStyleSheet(qss)
