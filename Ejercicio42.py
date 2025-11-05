# -*- coding: utf-8 -*-
"""
Requisitos:
Este programa crea una interfaz gráfica (GUI) con PyQt5 que permite 
realizar un 'ping' a una dirección IP o dominio y mostrar el resultado.
"""

# -------------------------------------------------------
# Librerías importadas y su función
# -------------------------------------------------------

import sys          # Permite acceder a funciones y parámetros del sistema, como sys.argv.
import platform     # Sirve para detectar el sistema operativo en el que se ejecuta el programa.
import subprocess   # Permite ejecutar comandos del sistema (como 'ping') y capturar su salida.

# ----- PyQt5 -----
from PyQt5.QtCore import Qt  # Contiene constantes y funciones relacionadas con el control de interfaz.
from PyQt5.QtWidgets import (  # Proporciona los widgets necesarios para construir la GUI.
    QApplication,  # Clase principal que gestiona la aplicación y el bucle de eventos.
    QWidget,       # Clase base para crear ventanas o componentes principales.
    QLabel,        # Widget para mostrar texto estático (etiquetas).
    QLineEdit,     # Campo de texto donde el usuario puede escribir (por ejemplo, la IP o dominio).
    QPushButton,   # Botón que el usuario puede presionar (en este caso, para ejecutar el ping).
    QTextEdit,     # Área de texto grande para mostrar la salida del ping.
    QVBoxLayout,   # Organiza los widgets verticalmente.
    QHBoxLayout,   # Organiza los widgets horizontalmente.
    QMessageBox,   # Permite mostrar mensajes emergentes (alertas, errores, advertencias).
)

# -------------------------------------------------------
# Clase principal de la aplicación
# -------------------------------------------------------

class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]   # En Windows se usa el parámetro -n
        else:  
            cmd = ["ping", "-c", "4", host]   # En Linux/macOS se usa -c

        try:
            # Ejecutamos el comando y capturamos stdout + stderr
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,   # Límite de tiempo para evitar bloqueos
            )
            salida = proceso.stdout if proceso.returncode == 0 else proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


# -------------------------------------------------------
# Punto de entrada de la aplicación
# -------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = PingApp()           # Instancia la ventana principal
    ventana.show()                # Muestra la ventana
    sys.exit(app.exec_())         # Ejecuta el bucle principal de eventos