import typing

from json import load
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from models.gui import styles


class ScaleChoice(QtWidgets.QScrollArea):
    def __init__(self, database, parent = None) -> None:
        super().__init__()
        self.p = parent
        self.database = database
        self.scales = [key for key in database]
        self.scale = self.scales[0]
        self.initialize()
        self.builder()

    def initialize(self):
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.horizontalScrollBar().hide()
        self.setStyleSheet("border: none;")

        self._layout = QtWidgets.QHBoxLayout()
        self._layout.setSpacing(10)
        self.body = QtWidgets.QWidget()

    def builder(self):

        self.buttons = []
        for key in self.scales:
            btn = QtWidgets.QLabel()
            btn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            btn.setContentsMargins(10, 10, 10, 10)
            btn.setMinimumSize(35, 35)
            self.setTitle(key, btn)
            btn.mousePressEvent = self.do_something(key)

            if key == self.scale:
                btn.setStyleSheet(styles.scaleChoiceButtonsSelected)
            else:
                btn.setStyleSheet(styles.scaleChoiceButtonsUnselected)

            self.buttons.append(btn)
            self._layout.addWidget(btn)

        self._layout.addStretch()
        self.body.setLayout(self._layout)
        self.setWidget(self.body)

    def do_something(self, something):
        def do_thing(*args):
            if something != self.scale:
                old_btn = self.buttons[self.scales.index(self.scale)]
                old_btn.setStyleSheet(styles.scaleChoiceButtonsUnselected)

                new_btn = self.buttons[self.scales.index(something)]
                new_btn.setStyleSheet(styles.scaleChoiceButtonsSelected)
                self.scale = something
                self.p.update_output()

        return do_thing
    
    @staticmethod
    def setTitle(text, label:QtWidgets.QLabel):
        n= 15
        inrange = (len(text)<=n+3)
        label.setText(text[:n+3*(inrange)]+"..."*(not inrange))
        #label.setToolTip(f"<i style='color: #FFFFFF;'>{text}<\i>")
        label.setToolTip(text)


