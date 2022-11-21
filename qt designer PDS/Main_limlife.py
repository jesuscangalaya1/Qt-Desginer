                        #!importaciones
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem
from messagebox import msg_error

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("registro.ui", self)
        self.setWindowTitle("Registro de 'LIMLIFE'")
        self.btnCuenta.clicked.connect(self.validar)

    def validar(self):
        nombres = self.txtNombre.text()
        apellidos = self.txtApellido.text()
        email = self.txtEmail.text()
        password = self.txtContra.text()

        if len(nombres) == 0 or len(apellidos) == 0 or len(email) == 0 or len(password) == 0:
            msg_error("Error", "No hay datos")
        else:
            self.hide()
            primera = login_Correcto(self)
            primera.show()


class login_Correcto(QMainWindow):
    def __init__(self, parent=None):
        super(login_Correcto, self).__init__(parent)
        uic.loadUi("login_correcto.ui", self)
        self.setWindowTitle("Registro Correcto ! ")
        self.btnSiguiente.clicked.connect(self.conectar_menu)
        self.btnSalir.clicked.connect(self.regresar)

    def conectar_menu(self):
        self.hide()
        segunda = ventanaMenu(self)
        segunda.show()

    def regresar(self):
        self.parent().show()
        self.close()


class ventanaMenu(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaMenu, self).__init__(parent)
        uic.loadUi("Menu_limlife.ui", self)
        self.setWindowTitle("menu  ! ")
        self.btnPlatillo.clicked.connect(self.conectar_platillo)
        self.btnPedido.clicked.connect(self.conectar_pedido)
        self.btnNosotros.clicked.connect(self.conectar_nosotros)

    def conectar_platillo(self):
        self.hide()
        segunda = ventanaPlatillo(self)
        segunda.show()

    def conectar_pedido(self):
        self.hide()
        tercera = ventanaPedido(self)
        tercera.show()

    def conectar_nosotros(self):
        self.hide()
        cuarta = ventanaNosotros(self)
        cuarta.show()


class ventanaPlatillo(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPlatillo, self).__init__(parent)
        uic.loadUi("platillos.ui", self)
        self.setWindowTitle("menu  ! ")
        self.comboPlatillo.currentIndexChanged.connect(self.ver_platillo)
        self.btnVer.clicked.connect(self.ver)
        self.btnBack.clicked.connect(self.regresar)

    def ver_platillo(self):
        plato = ["10$", "15$", "20$"]
        plato_2 = ["12$", "20$", "30$"]
        self.comboPrecio.clear()
        if self.comboPlatillo.currentText() == "Ceviche":
            self.comboPrecio.addItems(plato)
        elif self.comboPlatillo.currentText() == "Pachamanca":
            self.comboPrecio.addItems(plato_2)

    def ver(self):
        precio = self.comboPrecio.currentText()
        platillo = self.comboPlatillo.currentText()
        self.lblPrecio.setText(
            "El Platillo es '{}', y su precio es '{}'".format(platillo, precio))

    def regresar(self):
        self.parent().show()
        self.close()


class ventanaPedido(QMainWindow):
    filas = 1
    def __init__(self, parent=None):
        super(ventanaPedido, self).__init__(parent)
        uic.loadUi("Pedidos.ui", self)
        self.setWindowTitle("FORMULARIO DE PEDIDO ! ")
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnBack.clicked.connect(self.regresar)

    def registrar(self):
        nombre = self.txtNombre.text()
        platillo = self.txtPlatillo.text()
        direccion = self.txtDireccion.text()
        sede = self.comboSede.currentText()

        self.tblSalida.setRowCount(self.filas)  # ? ESTABLECER NRO DE FILAS
        self.tblSalida.verticalHeader().setVisible(False)  # ? OCULTA LA ENUMERACION DE LA TABLA

        self.tblSalida.setItem(self.filas - 1, 0, QTableWidgetItem(nombre))
        self.tblSalida.setItem(self.filas - 1, 1, QTableWidgetItem(platillo))
        self.tblSalida.setItem(self.filas - 1, 2, QTableWidgetItem(sede))
        self.tblSalida.setItem(self.filas - 1, 3, QTableWidgetItem(direccion))
        self.filas += 1

    def limpiar(self):
        self.txtNombre.clear()
        self.txtPlatillo.clear()
        self.txtDireccion.clear()
        self.comboSede.setCurrentText("Seleccione...")
    def regresar(self):
        self.parent().show()
        self.close()


class ventanaNosotros(QMainWindow):
    def __init__(self, parent=None):
        super(ventanaNosotros, self).__init__(parent)
        uic.loadUi("Nosotros.ui", self)
        self.setWindowTitle("SOBRE NOSOTROS... !")
        self.btnBack.clicked.connect(self.regresar)

    def regresar(self):
        self.parent().show()
        self.close()


app = QApplication(sys.argv)
_ventana = Login()
_ventana.show()
app.exec_()
