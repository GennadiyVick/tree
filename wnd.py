# -*- coding: utf-8 -*-
# Initializing mainwindow interface
# Copyright (C) 2020  Roganov G.V. roganovg@mail.ru
# 



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize



class Ui_MainWindow(object):
    def __init__(self, width=219, height=310):
        self.width = width
        self.height = height
    def setupUi(self, MainWindow):
        """Инициализируем графический интерфейс главного окна,
           создаём необходимые компоненты на форме и задаём их свойства."""        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(self.width, self.height))

        #фон окна прозрачный чтобы можно было в стиле установить любой цвет с альфой
        MainWindow.setStyleSheet("background: transparent;") 
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        #FramelessWindowHint - окно без рамок,
        #Qt.Tool - чтобы небыло видно иконки на панели задач
        MainWindow.setWindowFlags(Qt.FramelessWindowHint  | Qt.Tool) # | Qt.WindowStaysOnTopHint  | Qt.Tool

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


