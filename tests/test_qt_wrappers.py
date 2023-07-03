import unittest
import unreal_stylesheet
from pathlib import Path
from contextlib import suppress


# folder paths
TESTS_DIR = Path(__file__).parent
UI_DIR = TESTS_DIR / "sample_ui"

# test .ui files
EDITOR_UI = UI_DIR / "editor.ui"
MAIN_UI = UI_DIR / "main.ui"
PROGRESS_UI = UI_DIR / "progress.ui"
TREE_UI = UI_DIR / "tree.ui"
ui_paths = [EDITOR_UI, MAIN_UI, PROGRESS_UI, TREE_UI]


def test_pyqt5(ui_path):
    from PyQt5.QtWidgets import QApplication
    from PyQt5 import uic

    app = QApplication.instance() or QApplication([])
    unreal_stylesheet.setup()
    window = uic.loadUi(str(ui_path))
    window.show()
    QApplication.instance().exec_()
    return window


def test_pyside2(ui_path):
    from PySide2.QtWidgets import QApplication
    from PySide2 import QtUiTools
    from PySide2.QtCore import QFile

    app = QApplication.instance() or QApplication([])
    unreal_stylesheet.setup()
    loader = QtUiTools.QUiLoader()
    ui_file = QFile(str(ui_path))
    window = loader.load(ui_file)
    ui_file.close()
    window.show()
    QApplication.instance().exec_()
    return window


def test_pyside6(ui_path):
    from PySide6.QtWidgets import QApplication
    from PySide6 import QtUiTools
    from PySide6.QtCore import QFile
    app = QApplication.instance() or QApplication([])
    
    unreal_stylesheet.setup()
    loader = QtUiTools.QUiLoader()
    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.ReadOnly)  # Open the file in read-only mode
    window = loader.load(ui_file)
    ui_file.close()
    window.show()
    QApplication.instance().exec()
    return window


def test_pyqt6(ui_path):
    from PyQt6.QtWidgets import QApplication
    from PyQt6 import uic
    app = QApplication.instance() or QApplication([])

    unreal_stylesheet.setup()
    window = uic.loadUi(str(ui_path))
    window.show()
    QApplication.instance().exec()
    return window


def test_pyqt4(ui_path):
    # TODO this function is not tested, since PyQt4 is so ancient
    from PyQt4.QtGui import QApplication
    from PyQt4 import uic

    app = QApplication.instance() or QApplication([])
    unreal_stylesheet.setup()
    window = uic.loadUi(str(ui_path))
    window.show()
    QApplication.instance().exec_()
    return window


def test_pyside(ui_path):
    # TODO this function is not tested, since PySide is so ancient
    from PySide.QtGui import QApplication
    from PySide import QtUiTools
    from PySide.QtCore import QFile

    app = QApplication.instance() or QApplication([])
    unreal_stylesheet.setup()
    loader = QtUiTools.QUiLoader()
    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.ReadOnly)  # Open the file in read-only mode
    window = loader.load(ui_file)
    ui_file.close()
    window.show()
    QApplication.instance().exec_()
    return window


w = test_pyside2(EDITOR_UI)
