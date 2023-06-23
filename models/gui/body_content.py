import typing

from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtCore import QEvent, QObject

from models.gui.note_choice import NoteChoice
from models.gui.scale_choice import ScaleChoice
from models.gui import styles
from models.music.scale import Scale


class BodyContent(QtWidgets.QFrame):

    def __init__(self, database, parent: typing.Optional[QtWidgets.QWidget] = None) -> None:
        super().__init__(parent)
        self.database = database
        self.p = parent
        self.initialize()
        self.builder()

    def initialize(self):
        self.setGeometry(self.p.geometry()-QtCore.QMargins(5, 30, 5, 5))

        self._layout = QtWidgets.QVBoxLayout()
        self.setStyleSheet(styles.bodyContentStyle)
        self._layout.setContentsMargins(5, 10, 0, 5)

    def builder(self):
        self.noteLabel = QtWidgets.QLabel()
        self.noteLabel .setText(" choose a starting note:")

        self.noteList = NoteChoice(self)

        self.scaleLabel = QtWidgets.QLabel()
        self.scaleLabel .setText(" choose a scale:")

        self.scaleList = ScaleChoice(self.database, self)

        self.outputLabel = QtWidgets.QLabel()
        self.outputLabel.setText("output:")

        self.output = QtWidgets.QLabel()
        self.update_output()

        self._layout.addWidget(self.noteLabel)
        self._layout.addWidget(self.noteList)
        self._layout.addStretch(2)
        self._layout.addWidget(self.scaleLabel)
        self._layout.addWidget(self.scaleList)
        self._layout.addStretch(2)
        self._layout.addWidget(self.outputLabel)
        self._layout.addWidget(self.output)
        self._layout.addStretch(1)
        self.setLayout(self._layout)

    def update_output(self):
        _scale = self.scaleList.scale
        _note = self.noteList.note
        s = Scale(self.database[_scale])
        noteSeries = s.genarate_scale(_note)
        self.output.setText(" ".join(noteSeries))



