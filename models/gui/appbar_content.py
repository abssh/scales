import typing

from PyQt6.QtCore import QEvent, QObject

from models.gui import styles
from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets

class AppBarContent(QtWidgets.QWidget):
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = None) -> None:
        super().__init__(parent)
        self.Bsize = 25
        self._gripSize = self.window()._gripSize
        self.styles = styles.appbarStyle
        self._layout = QtWidgets.QHBoxLayout()
        self.mw = self.window()
        self.initialize()
        self.builder()
        self.mos_flag=None
        
    



    def initialize(self):
        pass


    def builder(self):
        bs = self.Bsize
        w = self.mw.width()

        # close
        self.closeB = QtWidgets.QPushButton()
        self.closeB.setText("⨯")
        self.closeB.setStyleSheet(self.styles["QPushButton"])
        self.closeB.resize(bs, bs)
        self.closeB.clicked.connect(lambda: self.mw.close())

        # hide
        self.hideB = QtWidgets.QPushButton()
        self.hideB.setText("─")
        self.hideB.setStyleSheet(self.styles["QPushButton"])
        self.hideB.resize(bs, bs)
        self.hideB.clicked.connect(lambda: self.mw.showMinimized())

        # title
        self.title = QtWidgets.QLabel()
        self.title.setStyleSheet(self.styles["QLabel"])
        self.title.setText("Scales")

        self._layout.setContentsMargins(7,1,7,7)
        self._layout.setSpacing(10)
        self._layout.addWidget(self.title)
        self._layout.addStretch()
        self._layout.addWidget(self.hideB)
        self._layout.addWidget(self.closeB)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.setLayout(self._layout)



    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.mos_flag=a0.pos()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.mos_flag:
            p1 = a0.pos()
            p2 = self.mos_flag
            rect = self.mw.geometry()
            rect.translate(p1.x()-p2.x(), p1.y()-p2.y())
            self.mw.setGeometry(rect)

    
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.mos_flag = None
        
    
