import typing

from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets

from models.gui.note_choice import NoteChoice
from models.gui.scale_choice import ScaleChoice
from models.music.scale import Scale


class BodyContent(QtWidgets.QVBoxLayout):

    def __init__(self, database, parent: typing.Optional[QtWidgets.QWidget] = None) -> None:
        super().__init__()
        self.database = database
        self.p = parent
        self.setContentsMargins(5, 0, 0, 5)
        self.builder()

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

        self.addWidget(self.noteLabel)
        self.addWidget(self.noteList)
        self.addStretch()
        self.addWidget(self.scaleLabel)
        self.addWidget(self.scaleList)
        self.addStretch()
        self.addWidget(self.outputLabel)
        self.addWidget(self.output)
        self.addStretch()
        self.p.setLayout(self)

    def update_output(self):
        _scale = self.scaleList.scale
        _note = self.noteList.note
        s = Scale(self.database[_scale])
        noteSeries = s.genarate_scale(_note)
        self.output.setText(" ".join(noteSeries))

