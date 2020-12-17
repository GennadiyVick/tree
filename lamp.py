#
# Lamp class, also this class using for snowing
# Copyright (C) 2020  Roganov G.V. roganovg@mail.ru
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
