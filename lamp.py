#
# Lamp class, also this class using for snowing
# Copyright (C) 2020  Roganov G.V. roganovg@mail.ru
# 

from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap
from math import sin
from random import randint

class Lamp:
    def __init__(self,scn,img,x=0,y=0,alpha=0.0):
        p = QPixmap(img)
        if scn == None:
            self.item = None
        else:
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

class Snow(Lamp):
    def __init__(self, scn, img, x=0, y=0, alpha=0.0, amplitude=2, frequence=20):
        super(Snow, self).__init__(scn, img, x, y, alpha)
        self.amplitude = amplitude
        self.frequence = frequence
        self.yoffset = randint(0,100)
        self.frequenceoffset = randint(-6,6)

    def hesitation(self):
        self.x += sin((self.y+self.yoffset) / (self.frequence+self.frequenceoffset)) * self.amplitude

    def reset(self):
        self.yoffset = randint(0,100)
        self.frequenceoffset = randint(-6,6)
        self.alpha = 1
