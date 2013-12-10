#!-*- coding: utf-8  -*-
from PyQt4.QtGui import QMainWindow, QColor, QTableView, QVBoxLayout, QPushButton , QDockWidget
from PyQt4.QtCore import Qt, QModelIndex, QAbstractTableModel, QVariant, SIGNAL


class PanelWidget(QDockWidget):
    '''central panel '''
    def __init__(self):
        super(QDockWidget, self).__init__()
        self.setFixedSize(800, 800)

