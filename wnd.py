# -*- coding: utf-8 -*-
# Initializing mainwindow interface
# Copyright (C) 2020  Roganov G.V. roganovg@mail.ru
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# some else...
# I bag your pardon for russian documentation of functions,
# if you need you can translate it with google


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


