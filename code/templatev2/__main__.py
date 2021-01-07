from PyQt5.QtWidgets import QApplication
from main import GoApp
import sys
# from main import GameSize

app = QApplication([])

# TODO - Make the GameSize come up first
# gameSize = GameSize()
# gameSize.show()

go = GoApp()
go.show()
sys.exit(app.exec_())
