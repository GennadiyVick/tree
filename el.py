#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMenu, QAction, QGraphicsScene
from PyQt5.QtCore import Qt, QPointF, QSize, QTimer
from PyQt5.QtGui import QPainter, QPixmap
import random
import wnd
import images
import math
from lamp import Lamp

class vect():
    def __init__(self,x=0,y=0):
        self.x = y
        self.y = x

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, qApp):
        super(MainWindow, self).__init__()
        self.ui = wnd.Ui_MainWindow() #создаём простой объект ui 
        self.ui.setupUi(self)
        self.qApp = qApp
        self.scn = QGraphicsScene(self)
        self.scn.setSceneRect(0,0, self.width()-2, self.height()-2)
        self.gv = QtWidgets.QGraphicsView(self)
        self.gv.setObjectName("gv")
        self.gv.setStyleSheet("border-width: 0px; border-style: none; outline:0px;")
        self.gv.setRenderHint(QPainter.Antialiasing);
        self.gv.setScene(self.scn)
        self.gv.setHorizontalScrollBarPolicy (Qt.ScrollBarAlwaysOff );
        self.gv.setVerticalScrollBarPolicy (Qt.ScrollBarAlwaysOff );        
        self.setCentralWidget(self.gv)
        self.gv.show()
        self.gv.mousePressEvent = self.mousePress
        self.gv.mouseMoveEvent = self.mouseMove
        
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        
        self.elimg = self.scn.addPixmap(QPixmap(":/images/Tree.png"))
        self.elimg.setTransformationMode(QtCore.Qt.SmoothTransformation)

        self.gv.setContextMenuPolicy(Qt.CustomContextMenu)
        self.gv.customContextMenuRequested.connect(self.initContextMenu)        
        
        self.mx = 0
        self.my = 0
        self.ps = None
        self.lamps = []
        self.setLamps()
        self.curlight = -1
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimer)
        self.timerinterval = 50
        self.timer.start(self.timerinterval)
        self.speed = 1
        self.lampturn = 1
        self.sparr = [0.1,0.4,0.6]
        self.cols = 6
        


    def initContextMenu(self, pos):
        menu = QMenu(self)
        menu.setStyleSheet("background: #333; color: white;")

        smenu = menu.addMenu("Скорость")
        act = QAction("Медленно",self)
        act.triggered.connect(self.slowspeed)
        smenu.addAction(act)
        act = QAction("Средне",self)
        act.triggered.connect(self.midspeed)
        smenu.addAction(act)
        act = QAction("Быстро",self)
        act.triggered.connect(self.fastspeed)
        smenu.addAction(act)
        
        kmenu = menu.addMenu("Переключения")
        act = QAction("По 1 лампочке",self)
        act.triggered.connect(self.onelamp)
        kmenu.addAction(act)
        act = QAction("По 2 лампочки",self)
        act.triggered.connect(self.twolamp)
        kmenu.addAction(act)        
        act = QAction("По 3 лампочки",self)
        act.triggered.connect(self.treelamp)
        kmenu.addAction(act)        
        act = QAction("По 4 лампочки",self)
        act.triggered.connect(self.forelamp)
        kmenu.addAction(act)       
        
        
        menu.addSeparator()
        act = QAction("Закрыть",self)
        act.triggered.connect(self.close)
        menu.addAction(act)
        
        p = self.mapToGlobal(pos)
        p.setX(p.x()+1)
        p.setY(p.y()+1)
        menu.exec_(p)        

    def slowspeed(self):
        self.speed = 0
    def midspeed(self):
        self.speed = 1
    def fastspeed(self):
        self.speed = 2
        
    def setlampsTurn(self,n):
        self.timer.stop()
        self.lampturn = n
        for lamps in self.lamps:
            for lamp in lamps:
                lamp.alpha = 0
                lamp.item.setOpacity(0)
        self.curlight =  -1
        self.timer.start(self.timerinterval)      
        
    def onelamp(self):
        self.setlampsTurn(1)
    def twolamp(self):
        self.setlampsTurn(2)
    def treelamp(self):
        self.setlampsTurn(3)
    def forelamp(self):
        self.setlampsTurn(4)        

    
        
    def setLamps(self):
        '''
        pts = [[vect(22,239),vect(86,281),vect(169,256),vect(46,224),vect(122,240),vect(50,178),
            vect(122,200),vect(74,157),vect(138,149),vect(119,133),vect(90,95),vect(85,47)],
            [vect(32,255),vect(110,281),vect(181,240),vect(59,237),vect(137,236),vect(62,192),
            vect(139,192),vect(87,165),vect(65,108),vect(136,123),vect(106,98),vect(102,54)],
            [vect(49,271),vect(133,274),vect(22,191),vect(79,242),vect(153,224),vect(82,200),
            vect(156,182),vect(106,165),vect(78,125),vect(126,92),vect(150,109),vect(119,45)],
            [vect(65,278),vect(152,268),vect(32,208),vect(100,243),vect(168,217),vect(103,204),
            vect(57,149),vect(124,160),vect(97,134),vect(73,83),vect(137,77),vect(99,25)]]
        '''
        pts = [[vect(25,238),vect(120,277),vect(44,218),vect(147,236),vect(82,201),vect(59,133),
                vect(149,153),vect(128,125),vect(113,94),vect(111,63)],
                [vect(36,250),vect(137,271),vect(54,232),vect(161,225),vect(101,204),vect(72,147),
                vect(160,137),vect(141,116),vect(126,92),vect(126,58)],
                [vect(51,263),vect(156,267),vect(71,241),vect(175,215),vect(121,202),vect(87,158),
                 vect(55,95),vect(158,105),vect(134,80),vect(93,32)],
                [vect(64,275),vect(172,256),vect(88,246),vect(43,157),vect(140,199),vect(100,169),
                 vect(74,114),vect(73,66),vect(149,71),vect(108,40)],
                [vect(80,277),vect(187,245),vect(108,245),vect(51,178),vect(154,192),vect(116,167),
                 vect(89,123),vect(86,79),vect(89,47),vect(121,34)],
                [vect(101,279),vect(28,198),vect(129,244),vect(66,191),vect(171,179),vect(135,161),
                 vect(108,127),vect(99,88),vect(100,59),vect(108,17)]]
        clrs = [["red1","red2","red3","red4","red5"],
                ["aqua1","aqua2","aqua2","aqua4","aqua5"],
                ["fuji1","fuji2","fuji3","fuji4","fuji5"],
                ["green1","green2","green3","green4","green5"],
                ["blue1","blue2","blue3","blue4","blue5"],
                ["yellow1","yellow2","yellow3","yellow4","yellow5"]]
        cv = 0                
        for c in range(len(pts)):
            lamps = []
            for v in pts[c]:
                lamp = Lamp(self.scn,":/images/"+clrs[c][cv]+".png",v.y,v.x)
                lamps.append(lamp)
                cv += 1
                if cv > 4: cv = 0
            self.lamps.append(lamps)

    def onTimer(self):
        finished = False
        nl = 0
        if self.curlight == self.cols-1: nl = 0
        else: nl = self.curlight+1
        
        for lamp in self.lamps[nl]:
            lamp.alpha += self.sparr[self.speed]
            if lamp.alpha >= 1.0:
                lamp.alpha = 1.0
                finished = True
            lamp.item.setOpacity(lamp.alpha)
        #for t in range(self.lampturn):
        if self.curlight>=0:
            n = self.curlight - self.lampturn + 1
            if n < 0: n = self.cols+n
            for lamp in self.lamps[n]:
                if lamp.alpha > 0:
                    lamp.alpha -= self.sparr[self.speed]
                    if lamp.alpha < 0: lamp.alpha = 0
                    lamp.item.setOpacity(lamp.alpha)
        if finished:
            self.curlight += 1
            if self.curlight >= self.cols: self.curlight = 0

            
    def mousePress(self,event):
        """Событие нажатия мыши на QGraphicsView,
           в данной функции  переменным присваивается глобальная
           позиция мыши и позиция окна, для того, чтобы при
           перемещении мыши вызывать перемещение главного окна."""
        self.mx = event.globalPos().x()
        self.my = event.globalPos().y()
        self.ps = self.pos()    
    def mouseMove(self,event):
        """Событие перемещения мыши на QGraphicsView,
           в данной функции перемещаем главное окно по экрану."""
        x = event.globalPos().x()-self.mx
        y = event.globalPos().y()-self.my
        self.move(self.ps.x()+x,self.ps.y()+y)   
        
    def closeEvent(self,event):
        self.qApp.quit()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(app)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()        
