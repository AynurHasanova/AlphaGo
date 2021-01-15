from PyQt5.QtWidgets import QApplication
from main import GoApp, GameSize
import sys


app = QApplication([])

# game_size = GameSize()
# game_size.show()

go = GoApp(7)
go.show()

sys.exit(app.exec_())
