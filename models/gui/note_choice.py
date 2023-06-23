import typing
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from models.gui import styles


class NoteChoice(QtWidgets.QScrollArea):
    notes = ["A",
             "A#",
             "B",
             "C",
             "C#",
             "D",
             "D#",
             "E",
             "F",
             "F#",
             "G",
             "G#"]

    def __init__(self, parent = None) -> None:
        super().__init__()

        self.p = parent
        self.note = "A"
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
        for n in self.notes:
            btn = QtWidgets.QLabel()
            btn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            btn.setFixedSize(35, 35)
            btn.setText(n)
            btn.setToolTip(f"note: {n}")
            btn.mousePressEvent = self.do_something(n)

            if n == self.note:
                btn.setStyleSheet(styles.noteChoiceButtonsSelected)
            else:
                btn.setStyleSheet(styles.noteChoiceButtonsUnselected)

            self.buttons.append(btn)
            self._layout.addWidget(btn)
        self._layout.addStretch()
        self.body.setLayout(self._layout)
        self.setWidget(self.body)


    def do_something(self, something):
        def do_thing(*args):
            if something != self.note:
                notes = self.notes
                old_btn = self.buttons[notes.index(self.note)]
                old_btn.setStyleSheet(styles.noteChoiceButtonsUnselected)

                new_btn = self.buttons[notes.index(something)]
                new_btn.setStyleSheet(styles.noteChoiceButtonsSelected)
                self.note = something
                self.p.update_output()

        return do_thing
