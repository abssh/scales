import typing

from json import load
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from models.gui import styles


class ScaleChoice(QtWidgets.QFrame):
    def __init__(self, database, parent = None) -> None:
        super().__init__()
        self.p = parent
        self.database = database
        self.scales = [key for key in database]
        self._layout = QtWidgets.QHBoxLayout()
        self.scale = self.scales[0]
        self.builder()

        self.buttons = []
        for key in self.scales:
            btn = QtWidgets.QLabel()
            btn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            btn.setMinimumSize(30, 30)
            btn.setText(key)
            btn.mousePressEvent = self.do_something(key)

            if key == self.scale:
                btn.setStyleSheet(styles.noteChoiceButtonsSelected)
            else:
                btn.setStyleSheet(styles.noteChoiceButtonsUnselected)

            self.buttons.append(btn)
            self._layout.addWidget(btn)

        self.setLayout(self._layout)

    def do_something(self, something):
        def do_thing(*args):
            if something != self.scale:
                old_btn = self.buttons[self.scales.index(self.scale)]
                old_btn.setStyleSheet(styles.noteChoiceButtonsUnselected)

                new_btn = self.buttons[self.scales.index(something)]
                new_btn.setStyleSheet(styles.noteChoiceButtonsSelected)
                self.scale = something
                self.p.update_output()


        return do_thing

    def builder(self):
        return
