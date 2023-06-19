from json import load
from PyQt6.QtWidgets import QApplication
from models.gui.main_window import MainWindow

with open("data/scales.json", "rb") as jf:
    database:dict = load(jf)


app = QApplication([])
mainWindow = MainWindow(database) 
mainWindow.show()
app.exec()
