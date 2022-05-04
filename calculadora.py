import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy



class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Minha primeira Calculadora')
        self.setFixedSize(600,600)
        self.cw= QWidget()
        self.grid= QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0,0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton(''), 1, 4, 1, 1)

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('Clear'), 2, 4, 1, 1,
            lambda: self.display.setText('')
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 3, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1])
        )

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 2, 1, 1,
            self.eval_igual
        )
        self.add_btn(QPushButton('/'), 4, 3, 1, 1)
        self.add_btn(QPushButton(''), 4, 4, 1, 1)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()

                )
            )

        else:
             btn.clicked.connect(funcao)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)



        self.setCentralWidget(self.cw)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Invalida')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()

