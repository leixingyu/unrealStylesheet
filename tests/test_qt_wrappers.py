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
    window = uic.loadUi(ui_path)
    window.show()
    QApplication.instance().exec_()
    return window




w = test_pyqt5(EDITOR_UI)
