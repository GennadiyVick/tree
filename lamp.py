#
# <one line to give the program's name and a brief idea of what it does.>
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
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QPointF, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

class Lamp:
    def __init__(self,scn,img,x=0,y=0,alpha=0.0):
        p = QPixmap(img)
        self.item = scn.addPixmap(p)
        self.item.setTransformationMode(Qt.SmoothTransformation)
        self.w = p.width()
        self.h = p.height()
        self.hw = self.w / 2
        self.hh = self.h / 2
        self.item.setPos(QPointF(x-self.hw,y-self.hh))
        self.item.setOpacity(alpha)
        self.x = x
        self.y = y
        self.alpha = alpha
