import typing
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from models.gui import styles


class NoteChoice(QtWidgets.QFrame):
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
        self._layout = QtWidgets.QHBoxLayout()
        self.note = "A"
        self.builder()

    def builder(self):
        self.buttons = []
        for n in self.notes:
            btn = QtWidgets.QLabel()
            btn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            btn.setFixedSize(30, 30)
            btn.setText(n)
            btn.mousePressEvent = self.do_something(n)

            if n == self.note:
                btn.setStyleSheet(styles.noteChoiceButtonsSelected)
            else:
                btn.setStyleSheet(styles.noteChoiceButtonsUnselected)

            self.buttons.append(btn)
            self._layout.addWidget(btn)

        self.setLayout(self._layout)

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
