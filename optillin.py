import sys
from PyQt5 import QtWidgets
import mainwindow
#Hasta acá se escribe siempre
#Se crea la clase que va a heredar propiedades de la clase QMainWindow
class MainWindowClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowClass, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_calcular.clicked.connect(self.calculo)

    def calculo(self):
        # Get Data
        print(self.ui.lineEdit_a.text())
        a = float(self.ui.lineEdit_a.text())/100
        b = float(self.ui.lineEdit_a.text())/100
        ancho = float(self.ui.lineEdit_ancho.text())/100
        try:
            costoTela = float(self.ui.lineEdit_costo.text())
        except:
            pass


        uni_ancho= int(ancho/b)
        metros = 1
        while True:
            n = metros/a
            n_int = int(n)

            if n==n_int:
                uni_largo = n_int
                total_uni = uni_largo*uni_ancho
                unidad_metro = int(total_uni/metros)
                try:
                    costo_unidad = (costoTela/unidad_metro)
                except:
                    costo_unidad = 'No Info'

                self.ui.label_totalPiezas.setText(str(total_uni))
                self.ui.label_totalMetros.setText(str(metros))
                self.ui.label_piezasXmetro.setText(str(unidad_metro))
                self.ui.label_costoPieza.setText(str(costo_unidad))
                break
            else:
                metros = metros +1


aplicacion = QtWidgets.QApplication(sys.argv) ##esto es estandar

## Se crea el objeto de la clase MainWindowClass y se muestra en la pantalla
ventana = MainWindowClass()
ventana.show()
aplicacion.exec_() ## esto es estandar
