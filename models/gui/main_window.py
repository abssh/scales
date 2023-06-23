import typing

from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtCore import QEvent

from models.gui import AppBarContent, BodyContent, styles




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, database, parent: typing.Optional[QtWidgets.QWidget] = None, flags: QtCore.Qt.WindowType =
                 QtCore.Qt.WindowType.FramelessWindowHint) -> None:
        super().__init__(parent, flags)
        self._gripSize = 5
        self.database = database
        self.initialize()
        self.builder()
        self.resizeingfuncs=None
        self.pivot = None

    def initialize(self):
        self.setMinimumSize(500, 400)
        self.resize(500, 400)

        # self._appbar = self.body = QtWidgets.QFrame(self)
        # self._appbar.setGeometry(0, 0, self.width(), 30)
        # self._appbar.setStyleSheet(styles.appbarStyle["QFrame"])





    def builder(self):
        AppBarContent(self)

        BodyContent(self.database, self)

    
    
    def eventFilter(self, source, event: QEvent):
        if event.type() == QtCore.QEvent.Type.MouseMove:
            if event.buttons() == QtCore.Qt.MouseButton.NoButton:
                pos = event.pos()
                g = self._gripSize
                w = self.width()
                h = self.height()

                if pos.x() <= g and source == self:
                    if pos.y() <= g:
                        self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
                    elif pos.y() >= h-g:
                        self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
                
                    else:
                        self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                        
                elif pos.x() >= w-g and source == self:

                    if pos.y() <= g:
                        self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
                    elif pos.y() >= h-g:
                        self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
                    else:
                        self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)

                elif pos.y() <= g and source == self:
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
                elif pos.y() >= h-g and source == self:
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)

                else:
                    self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        return super().eventFilter(source, event)
    
    
    def resizeLeft(self, delta):
        width = max(self.minimumWidth(), self.width() - delta.x())
        geo = self.geometry()
        geo.setLeft(geo.right() - width)
        self.setGeometry(geo)

    def resizeTop(self, delta):
        height = max(self.minimumHeight(), self.height() - delta.y())
        geo = self.geometry()
        geo.setTop(geo.bottom() - height)
        self.setGeometry(geo)

    def resizeRight(self, delta):
        width = max(self.minimumWidth(), self.width() + delta.x())
        self.resize(width, self.height())

    def resizeBottom(self, delta):
        height = max(self.minimumHeight(), self.height() + delta.y())
        self.resize(self.width(), height)

    
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        pos = e.pos()
        self.pivot = pos
        g = self._gripSize
        w = self.width()
        h = self.height()
        if pos.x() <= g:
            self.resizeingfuncs = [self.resizeLeft]
            if pos.y() <= g:
                self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
                self.resizeingfuncs.append(self.resizeTop)
            elif pos.y() >= h-g:
                self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
                self.resizeingfuncs.append(self.resizeBottom)
        
                
        elif pos.x() >= w-g:
            self.resizeingfuncs = [self.resizeRight]
            if pos.y() <= g:
                self.resizeingfuncs.append(self.resizeTop)
            elif pos.y() >= h-g:
                self.resizeingfuncs.append(self.resizeBottom)
            

        elif pos.y() <= g:
            self.resizeingfuncs = [self.resizeTop]
        elif pos.y() >= h-g:
            self.resizeingfuncs = [self.resizeBottom]
            
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.pivot is not None:
            delta = e.pos() - self.pivot
            if self.resizeingfuncs:
                for func in self.resizeingfuncs:
                    func(delta)
        self.pivot = e.pos()
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.pivot = None
        self.resizeingfuncs = None
        return super().mouseReleaseEvent(e)


