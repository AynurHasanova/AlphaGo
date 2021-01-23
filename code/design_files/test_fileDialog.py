from PyQt5 import QtGui, QtWidgets
import pickle
 
# Initialize the application
app = QtWidgets.QApplication([])

widget = QtWidgets.QWidget()
widget.setFixedSize(300, 300)
widget.show()

fileName, _ = QtWidgets.QFileDialog.getSaveFileName(widget, "All files", '/home/nerdraven', "Python Files (*.py);; All Files (*)")
print(fileName)

a = []
a.append("djdkdjdjd")
with open(fileName, 'wb') as fp:
    pickle.dump(a, fp)

app.exec_()