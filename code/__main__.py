from PyQt5.QtWidgets import QApplication
from main import GoApp
import sys

app = QApplication([])

go = GoApp()
go.show()
sys.exit(app.exec_())
