import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Hola Mundo en PyQt5")
ventana.setGeometry(100, 100, 400, 200)

etiqueta = QLabel("<h1>¡Hola, Mundo!</h1>", ventana)

ventana.show()
sys.exit(app.exec_())
