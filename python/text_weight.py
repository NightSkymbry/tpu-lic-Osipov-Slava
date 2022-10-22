import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial


x = {
    0: 'i',
    1: 'k',
    2: 'k',
    3: 'I',
    -1: 'un'
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.types = {
            'i': 0,
            'k': 0,
            'I': 0,
            'un': 0
        }

        self.types_r = {
            1: -1,
            2: -1,
            3: -1
        }

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 212)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.given = QtWidgets.QLabel(self.centralwidget)
        self.given.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.given.setFont(font)
        self.given.setObjectName("given")

        self.given_1_type = QtWidgets.QComboBox(self.centralwidget)
        self.given_1_type.setGeometry(QtCore.QRect(10, 50, 73, 22))
        self.given_1_type.setCurrentText("")
        self.given_1_type.setObjectName("given_1_type")
        self.given_1_type.addItem("")
        self.given_1_type.addItem("")
        self.given_1_type.addItem("")
        self.given_1_type.addItem("")
        self.given_1_type.setCurrentIndex(-1)
        self.given_1_type.currentIndexChanged.connect(partial(self.type_changed, cb=1))

        # self.given_1_type.model().item(1).setEnabled(False)
        self.toFind_type = QtWidgets.QComboBox(self.centralwidget)
        self.toFind_type.setGeometry(QtCore.QRect(10, 170, 73, 22))
        self.toFind_type.setCurrentText("")
        self.toFind_type.setObjectName("toFind_type")
        self.toFind_type.addItem("")
        self.toFind_type.addItem("")
        self.toFind_type.addItem("")
        self.toFind_type.addItem("")
        self.toFind_type.setCurrentIndex(-1)
        self.toFind_type.currentIndexChanged.connect(partial(self.type_changed, cb=3))

        self.given_2_type = QtWidgets.QComboBox(self.centralwidget)
        self.given_2_type.setGeometry(QtCore.QRect(10, 80, 73, 22))
        self.given_2_type.setCurrentText("")
        self.given_2_type.setObjectName("given_2_type")
        self.given_2_type.addItem("")
        self.given_2_type.addItem("")
        self.given_2_type.addItem("")
        self.given_2_type.addItem("")
        self.given_2_type.setCurrentIndex(-1)
        self.given_2_type.currentIndexChanged.connect(partial(self.type_changed, cb=2))

        self.given_1_num = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.given_1_num.setEnabled(True)
        self.given_1_num.setGeometry(QtCore.QRect(100, 50, 151, 22))
        self.given_1_num.setObjectName("given_1_num")
        self.given_1_num.setMaximum(1000000)
        self.given_1_num.hide()

        self.given_2_num = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.given_2_num.setEnabled(True)
        self.given_2_num.setGeometry(QtCore.QRect(100, 80, 151, 22))
        self.given_2_num.setObjectName("given_2_num")
        self.given_2_num.setMaximum(1000000)
        self.given_2_num.hide()

        self.given_1_text = QtWidgets.QLineEdit(self.centralwidget)
        self.given_1_text.setGeometry(QtCore.QRect(100, 50, 481, 22))
        self.given_1_text.setObjectName("given_1_text")
        self.given_1_text.hide()

        self.given_2_text = QtWidgets.QLineEdit(self.centralwidget)
        self.given_2_text.setGeometry(QtCore.QRect(100, 80, 481, 22))
        self.given_2_text.setObjectName("given_2_text")
        self.given_2_text.hide()

        self.given_1_unit = QtWidgets.QComboBox(self.centralwidget)
        self.given_1_unit.setGeometry(QtCore.QRect(260, 50, 73, 22))
        self.given_1_unit.setObjectName("given_1_unit")
        self.given_1_unit.addItem("")
        self.given_1_unit.addItem("")
        self.given_1_unit.hide()
        self.given_1_unit.setCurrentIndex(0)

        self.given_2_unit = QtWidgets.QComboBox(self.centralwidget)
        self.given_2_unit.setGeometry(QtCore.QRect(260, 80, 73, 22))
        self.given_2_unit.setObjectName("given_2_unit")
        self.given_2_unit.addItem("")
        self.given_2_unit.addItem("")
        self.given_2_unit.setCurrentIndex(0)
        self.given_2_unit.hide()

        self.toFind = QtWidgets.QLabel(self.centralwidget)
        self.toFind.setGeometry(QtCore.QRect(10, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toFind.setFont(font)
        self.toFind.setObjectName("toFind")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 120, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 130, 16, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(100, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer.setFont(font)
        self.answer.setObjectName("answer")

        self.answer_text = QtWidgets.QLabel(self.centralwidget)
        self.answer_text.setGeometry(QtCore.QRect(104, 170, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_text.setFont(font)
        self.answer_text.setObjectName("answer_text")

        self.answer_unit = QtWidgets.QComboBox(self.centralwidget)
        self.answer_unit.setGeometry(QtCore.QRect(480, 170, 121, 31))
        self.answer_unit.setObjectName("answer_unit")
        self.answer_unit.addItem("")
        self.answer_unit.addItem("")
        self.answer_unit.addItem("")
        self.answer_unit.addItem("")
        self.answer_unit.addItem("")
        self.answer_unit.hide()
        self.answer_unit.setCurrentIndex(0)
        self.answer_unit.currentIndexChanged.connect(self.calc)

        self.answer_calc = QtWidgets.QPushButton(self.centralwidget)
        self.answer_calc.setGeometry(QtCore.QRect(220, 130, 93, 31))
        self.answer_calc.setObjectName("answer_calc")
        self.answer_calc.setEnabled(False)
        self.answer_calc.clicked.connect(self.calc)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Д/З"))
        self.given.setText(_translate("MainWindow", "Дано:"))
        self.given_1_type.setItemText(0, _translate("MainWindow", "i"))
        self.given_1_type.setItemText(1, _translate("MainWindow", "k"))
        self.given_1_type.setItemText(2, _translate("MainWindow", "k (text)"))
        self.given_1_type.setItemText(3, _translate("MainWindow", "I"))
        self.toFind_type.setItemText(0, _translate("MainWindow", "i"))
        self.toFind_type.setItemText(1, _translate("MainWindow", "k"))
        self.toFind_type.setItemText(2, _translate("MainWindow", "k"))
        self.toFind_type.setItemText(3, _translate("MainWindow", "I"))
        self.given_2_type.setItemText(0, _translate("MainWindow", "i"))
        self.given_2_type.setItemText(1, _translate("MainWindow", "k"))
        self.given_2_type.setItemText(2, _translate("MainWindow", "k (text)"))
        self.given_2_type.setItemText(3, _translate("MainWindow", "I"))
        self.given_1_unit.setCurrentText(_translate("MainWindow", "бит (а)"))
        self.given_1_unit.setItemText(0, _translate("MainWindow", "бит (а)"))
        self.given_1_unit.setItemText(1, _translate("MainWindow", "Байт (а)"))
        self.given_2_unit.setCurrentText(_translate("MainWindow", "бит (а)"))
        self.given_2_unit.setItemText(0, _translate("MainWindow", "бит (а)"))
        self.given_2_unit.setItemText(1, _translate("MainWindow", "Байт (а)"))
        self.toFind.setText(_translate("MainWindow", "Найти:"))
        self.answer.setText(_translate("MainWindow", "Ответ:"))
        self.answer_unit.setItemText(0, _translate("MainWindow", "бит (а)"))
        self.answer_unit.setItemText(1, _translate("MainWindow", "байт (а)"))
        self.answer_unit.setItemText(2, _translate("MainWindow", "КБ"))
        self.answer_unit.setItemText(3, _translate("MainWindow", "МБ"))
        self.answer_unit.setItemText(4, _translate("MainWindow", "ГБ"))
        self.answer_text.setText(_translate("MainWindow", ""))
        self.answer_calc.setText(_translate("MainWindow", "Рассчитать"))

    def type_changed(self, cb): # извиняюсь, но это ******. делал впервые подобное и вечером. мозги вынесло, но работает как-тою
        match cb:
            case 1:
                match ind := self.given_1_type.currentIndex():
                    case 0:
                        if self.types['i'] != 0:
                            match self.types['i']:
                                case 2:
                                    self.types[x[self.types_r[1]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[1])
                                case 3:
                                    self.types[x[self.types_r[1]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[1])
                        self.types['i'] = 1
                        self.types_r[1] = 0
                        self.given_1_num.show()
                        self.given_1_unit.show()
                        self.given_1_text.hide()
                    case 3:
                        if self.types['I'] != 0:
                            match self.types['I']:
                                case 2:
                                    self.types[x[self.types_r[1]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[1])
                                case 3:
                                    self.types[x[self.types_r[1]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[1])
                        self.types['I'] = 1
                        self.types_r[1] = 3
                        self.given_1_num.show()
                        self.given_1_unit.show()
                        self.given_1_text.hide()
                    case 1:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 2:
                                    self.types[x[self.types_r[1]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[1])
                                case 3:
                                    self.types[x[self.types_r[1]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[1])
                        self.types['k'] = 1
                        self.types_r[1] = 1
                        self.given_1_num.show()
                        self.given_1_unit.hide()
                        self.given_1_text.hide()
                    case 2:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 2:
                                    self.types[x[self.types_r[1]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[1])
                                case 3:
                                    self.types[x[self.types_r[1]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[1])
                        self.types['k'] = 1
                        self.types_r[1] = 2
                        self.given_1_num.hide()
                        self.given_1_unit.hide()
                        self.given_1_text.show()
                    case -1:
                        self.given_1_num.hide()
                        self.given_1_unit.hide()
                        self.given_1_text.hide()
                        self.types_r[1] = -1
            case 2:
                match ind := self.given_2_type.currentIndex():
                    case 0:
                        if self.types['i'] != 0:
                            match self.types['i']:
                                case 1:
                                    self.types[x[self.types_r[2]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[2])
                                case 3:
                                    self.types[x[self.types_r[2]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[2])
                        self.types['i'] = 2
                        self.types_r[2] = 0
                        self.given_2_num.show()
                        self.given_2_unit.show()
                        self.given_2_text.hide()
                    case 3:
                        if self.types['I'] != 0:
                            match self.types['I']:
                                case 1:
                                    self.types[x[self.types_r[2]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[2])
                                case 3:
                                    self.types[x[self.types_r[2]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[2])
                        self.types['I'] = 2
                        self.types_r[2] = 3
                        self.given_2_num.show()
                        self.given_2_unit.show()
                        self.given_2_text.hide()
                    case 1:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 1:
                                    self.types[x[self.types_r[2]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[2])
                                case 3:
                                    self.types[x[self.types_r[2]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[2])
                        self.types['k'] = 2
                        self.types_r[2] = 1
                        self.given_2_num.show()
                        self.given_2_unit.hide()
                        self.given_2_text.hide()
                    case 2:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 1:
                                    self.types[x[self.types_r[2]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[2])
                                case 3:
                                    self.types[x[self.types_r[2]]] = 3
                                    self.toFind_type.setCurrentIndex(self.types_r[2])
                        self.types['k'] = 2
                        self.types_r[2] = 2
                        self.given_2_num.hide()
                        self.given_2_unit.hide()
                        self.given_2_text.show()
                    case -1:
                        self.given_2_num.hide()
                        self.given_2_unit.hide()
                        self.given_2_text.hide()
                        self.types_r[2] = -1
            case 3:
                match ind := self.toFind_type.currentIndex():
                    case 0:
                        if self.types['i'] != 0:
                            match self.types['i']:
                                case 1:
                                    self.types[x[self.types_r[3]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[3])
                                case 2:
                                    self.types[x[self.types_r[3]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[3])
                        self.types['i'] = 3
                        self.types_r[3] = 0
                    case 3:
                        if self.types['I'] != 0:
                            match self.types['I']:
                                case 1:
                                    self.types[x[self.types_r[3]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[3])
                                case 2:
                                    self.types[x[self.types_r[3]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[3])
                        self.types['I'] = 3
                        self.types_r[3] = 3
                    case 1:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 1:
                                    self.types[x[self.types_r[3]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[3])
                                case 2:
                                    self.types[x[self.types_r[3]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[3])
                        self.types['k'] = 3
                        self.types_r[3] = 1
                    case 2:
                        if self.types['k'] != 0:
                            match self.types['k']:
                                case 1:
                                    self.types[x[self.types_r[3]]] = 1
                                    self.given_1_type.setCurrentIndex(self.types_r[3])
                                case 2:
                                    self.types[x[self.types_r[3]]] = 2
                                    self.given_2_type.setCurrentIndex(self.types_r[3])
                        self.types['k'] = 3
                        self.types_r[3] = 2
                    case -1:
                        self.types_r[3] = -1
        if self.types_r[3] > -1 and self.types_r[2] > -1 and self.types_r[1] > -1:
            self.answer_calc.setEnabled(True)
        # print(self.types, self.types_r, end='\n\n')

    def calc(self):
        match self.toFind_type.currentIndex():
            case 3:
                self.answer_text.show()
                self.answer_unit.show()
                match i := self.answer_unit.currentIndex():
                    case 0:
                        mn = 1
                    case _:
                        mn = 8 * (1024 ** (i - 1))
                self.answer_text.setText(f'{((self.given_1_num.value() * (8 ** self.given_1_unit.currentIndex() if self.given_1_type.currentIndex() != 1 else 1)) if self.given_1_type.currentIndex() != 2 else len(self.given_1_text.text())) * ((self.given_2_num.value() * (8 * self.given_2_unit.currentIndex() if self.given_2_type.currentIndex() != 1 else 1)) if self.given_2_type.currentIndex() != 2 else len(self.given_2_text.text())) / mn}')
            case 0:
                self.answer_text.show()
                self.answer_unit.show()
                match i := self.answer_unit.currentIndex():
                    case 0:
                        mn = 1
                    case _:
                        mn = 8 * (1024 ** (i - 1))
                if self.given_1_type.currentIndex() == 3:
                    self.answer_text.setText(f'{(self.given_1_num.value() * (8 ** self.given_1_unit.currentIndex())) / (self.given_2_num.value() if self.given_2_type.currentIndex() != 2 else len(self.given_2_text.text())) / mn}')
                else:
                    self.answer_text.setText(f'{(self.given_2_num.value() * (8 ** self.given_2_unit.currentIndex())) / (self.given_1_num.value() if self.given_1_type.currentIndex() != 2 else len(self.given_1_text.text())) / mn}')
            case 1 | 2:
                self.answer_text.show()
                self.answer_unit.hide()
                if self.given_1_type.currentIndex() == 3:
                    self.answer_text.setText(f'{(self.given_1_num.value() * (8 ** self.given_1_unit.currentIndex())) / (self.given_2_num.value() * (8 ** self.given_2_unit.currentIndex()))} символов')
                else:
                    self.answer_text.setText(f'{(self.given_2_num.value() * (8 ** self.given_2_unit.currentIndex())) / (self.given_1_num.value() * (8 ** self.given_1_unit.currentIndex()))} символов')


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    app.exec()



if __name__ == '__main__':
    run()
