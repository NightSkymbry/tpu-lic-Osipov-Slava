import csv
from functools import partial
from typing import NamedTuple
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os
import random
from threading import Timer


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


class Word(NamedTuple):
    English: str
    Russian: str


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        self.words: list[Word] = []
        self.indexes: list[int] = []
        self.confirming: list[int] = []
        self.cur_index: int = -1
        self.cur_index_index: int = -1
        self.mode: str = 'Learn'
        self.timer_obj: RepeatingTimer = RepeatingTimer(1.0, self.tick)
        self.timer_counter: int = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.word_box = QtWidgets.QLabel(self.centralwidget)
        self.word_box.setGeometry(QtCore.QRect(20, 85, 760, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.word_box.setFont(font)
        self.word_box.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.word_box.setText("")
        self.word_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_box.setObjectName("word_box")

        self.unit_loading_text = QtWidgets.QLabel(self.centralwidget)
        self.unit_loading_text.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unit_loading_text.setFont(font)
        self.unit_loading_text.setObjectName("unit_loading_text")
        # self.unit_loading_text.setEnabled(True)
        # self.unit_loading_text.show()

        self.load_unit = QtWidgets.QPushButton(self.centralwidget)
        self.load_unit.setGeometry(QtCore.QRect(430, 10, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.load_unit.setFont(font)
        self.load_unit.setObjectName("load_unit")
        self.load_unit.setEnabled(False)

        self.unit_to_load = QtWidgets.QComboBox(self.centralwidget)
        self.unit_to_load.setGeometry(QtCore.QRect(120, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unit_to_load.setFont(font)
        self.unit_to_load.setObjectName("unit_to_load")

        self.answer_box = QtWidgets.QLabel(self.centralwidget)
        self.answer_box.setGeometry(QtCore.QRect(20, 300, 760, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.answer_box.setFont(font)
        self.answer_box.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.answer_box.setText("")
        self.answer_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.answer_box.setObjectName("answer_box")

        self.look_answer_button = QtWidgets.QPushButton(self.centralwidget)
        self.look_answer_button.setGeometry(QtCore.QRect(325, 250, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.look_answer_button.setFont(font)
        self.look_answer_button.setObjectName("look_answer_button")
        self.look_answer_button.setEnabled(False)

        self.correct_button = QtWidgets.QPushButton(self.centralwidget)
        self.correct_button.setGeometry(QtCore.QRect(192, 510, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.correct_button.setFont(font)
        self.correct_button.setObjectName("correct_button")
        self.correct_button.setEnabled(False)

        self.wrong_button = QtWidgets.QPushButton(self.centralwidget)
        self.wrong_button.setGeometry(QtCore.QRect(496, 510, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong_button.setFont(font)
        self.wrong_button.setObjectName("wrong_button")
        self.wrong_button.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_units()
        self.unit_to_load.setCurrentIndex(-1)

        self.unit_to_load.currentIndexChanged.connect(partial(self.load_unit.setEnabled, True))
        self.load_unit.clicked.connect(self.load_words)
        self.look_answer_button.clicked.connect(self.view_answer)
        self.correct_button.clicked.connect(self.correct)
        self.wrong_button.clicked.connect(self.wrong)


    def tick(self):
        if self.timer_counter:
            self.timer_counter -= 1
            self.answer_box.setText(str(self.timer_counter))
        else:
            self.timer_counter = 30
            self.update_word()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.unit_loading_text.setText(_translate("MainWindow", "Unit to load:"))
        self.load_unit.setText(_translate("MainWindow", "+ Добавить"))
        self.look_answer_button.setText(_translate("MainWindow", "Посмотреть ответ"))
        self.correct_button.setText(_translate("MainWindow", "Правильно"))
        self.wrong_button.setText(_translate("MainWindow", "Неверно"))


    def load_units(self):
        for file in os.listdir('./units'):
            d = os.path.splitext(file)
            if d[1] == '.csv':
                self.unit_to_load.addItem(d[0])


    def load_words(self):
        # self.timer_obj.start()
        x = len(self.words)
        with open(f'./units/{self.unit_to_load.currentText()}.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader, len(self.words)):
                self.words.append(Word(row[0], row[1]))
                for _ in range(2):
                    self.indexes.append(i)
        if not x: self.update_word()


    def switch_to_confirming_mode(self):
        if self.mode == 'Dictation':
            self.mode = 'Confirming_prep'
            self.look_answer_button.setText('Начать проверку')
            self.word_box.setText('Готово')
            self.answer_box.setText('')
            self.timer_obj.cancel()
        elif self.mode == 'Confirming_prep':
            self.mode = 'Confirming'
            self.look_answer_button.setText('Дальше')
            self.update_word()


    def switch_to_dictation_mode(self):
        if self.mode == 'Learn':
            self.mode = 'Dictation_prep'
            self.confirming.clear()
            self.indexes: list[int] = [i for i in range(len(self.words))]
            self.unit_loading_text.hide()
            self.unit_to_load.hide()
            self.load_unit.hide()
            self.correct_button.hide()
            self.wrong_button.hide()
            self.look_answer_button.setEnabled(True)
            self.look_answer_button.setText('Начать')
            self.word_box.setText('Диктант')
            self.answer_box.setText('')

        elif self.mode == 'Dictation_prep':
            self.mode = 'Dictation'
            self.timer_counter = 30
            self.timer_obj.start()
            self.update_word()
            self.look_answer_button.setText('Дальше')


    def update_word(self):
        if self.mode == 'Learn':
            if len(self.indexes):
                self.cur_index_index = random.randint(0, len(self.indexes) - 1)
                self.cur_index = self.indexes[self.cur_index_index]
                self.word_box.setText(self.words[self.cur_index].Russian)

                self.look_answer_button.setEnabled(True)
                self.correct_button.setEnabled(False)
                self.wrong_button.setEnabled(False)
                self.answer_box.setText('')
            else:
                self.switch_to_dictation_mode()

        elif self.mode == 'Dictation':
            if self.indexes:
                self.answer_box.setText(str(self.timer_counter))
                self.cur_index_index = random.randint(0, len(self.indexes) - 1)
                self.cur_index = self.indexes[self.cur_index_index]
                self.confirming.append(self.cur_index)
                self.word_box.setText(self.words[self.cur_index].Russian)
                del self.indexes[self.cur_index_index]
            else:
                self.switch_to_confirming_mode()

        elif self.mode == 'Confirming':
            if self.confirming:
                self.word_box.setText(self.words[self.confirming[0]].Russian)
                self.answer_box.setText(self.words[self.confirming[0]].English)
                del self.confirming[0]
            else:
                self.setupUi(self.mainWindow)


    def view_answer(self):
        if self.mode == 'Learn':
            self.look_answer_button.setEnabled(False)
            self.correct_button.setEnabled(True)
            self.wrong_button.setEnabled(True)

            self.answer_box.setText(self.words[self.cur_index].English)

        elif self.mode == 'Dictation':
            self.timer_counter += 30
            if self.timer_counter >= 60:
                self.timer_counter = 60
            self.update_word()

        elif self.mode == 'Confirming':
            self.update_word()

        elif self.mode == 'Dictation_prep':
            self.switch_to_dictation_mode()

        elif self.mode == 'Confirming_prep':
            self.switch_to_confirming_mode()



    def correct(self):
        del self.indexes[self.cur_index_index]
        self.update_word()


    def wrong(self):
        self.indexes.append(self.cur_index)
        self.indexes.append(self.cur_index)
        self.update_word()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    app.exec()
