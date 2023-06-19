import typing

from PyQt6 import QtCore
from PyQt6 import QtWidgets

from models.gui import AppBarContent, BodyContent, styles


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, database, parent: typing.Optional[QtWidgets.QWidget] = None, flags: QtCore.Qt.WindowType =
                 QtCore.Qt.WindowType.FramelessWindowHint) -> None:
        super().__init__(parent, flags)
        self._gripSize = 5
        self.database = database
        self.initialize()
        self.builder()

    def initialize(self):
        self.setMinimumSize(300, 200)
        self.resize(500, 400)

        self._appbar = self.body = QtWidgets.QFrame(self)
        self._appbar.setGeometry(0, 0, self.width(), 30)
        self._appbar.setStyleSheet(styles.appbarStyle["QFrame"])

        self.body = QtWidgets.QFrame(self)
        self.body.setGeometry(self.geometry()-QtCore.QMargins(5, 30, 5, 5))

    def builder(self):
        AppBarContent(self._appbar)

        BodyContent(self.database, self.body)
