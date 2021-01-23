from PyQt5 import QtGui, QtWidgets
 
# Initialize the application
app = QtWidgets.QApplication([])
 
# The Bitmap
bitmap = QtGui.QBitmap('../assets/round-ball.bmp')
cursor = QtGui.QCursor(bitmap)

# The Widget
widget = QtWidgets.QLabel('Ndkdjdldjdljdkdjd')
widget.setFixedSize(300, 300)
widget.setCursor(cursor)

widget.show()

app.exec_()
