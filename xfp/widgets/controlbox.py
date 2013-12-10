#!-*- coding: utf-8  -*-

from PyQt4.QtGui import QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QWidget
from PyQt4.QtCore import QState, QPointF, QStateMachine, Qt, QObject, SIGNAL, SLOT, QThread


class ControlBox(QGraphicsView):
    ''' dynamic control box at bottom '''
    def __init__(self, parent=None):
        super(QGraphicsView, self).__init__(parent)
        self.scene = QGraphicsScene(0, 0, 0, 0)
        self.setScene(self.scene)
        self.resize(1000,100)



















