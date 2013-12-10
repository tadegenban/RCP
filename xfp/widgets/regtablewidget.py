#!-*- coding: utf-8  -*-

from .. import qtall as qt4


class RegTableModel(qt4.QAbstractTableModel):
    ''' register table model  '''
    def __init__(self, parent=None):
        super(qt4.QAbstractTableModel, self).__init__(parent)
        self.registers = range(128)

    def flags(self, index):
        col = index.column()
        if not index.isValid():
            return qt4.Qt.ItemIsEnabled
        if (col % 2):
            return qt4.Qt.ItemFlags(qt4.QAbstractTableModel.flags(self, index) | qt4.Qt.ItemIsEditable)
        else:
            return qt4.Qt.ItemFlags(qt4.QAbstractTableModel.flags(self, index) &
                                    ~qt4.Qt.ItemIsEditable)

    def data(self, index, role=qt4.Qt.DisplayRole):
        if (not index.isValid() or not (0 <= index.row)):
            return qt4.QVariant()
        row = index.row()
        col = index.column()
        if role == qt4.Qt.DisplayRole:
            if (col % 2):
                return qt4.QVariant(self.registers[(col - 1) * self.rowCount() / 2 + row])
            else:
                return qt4.QVariant(col * self.rowCount() / 2 + row)
        if role == qt4.Qt.TextAlignmentRole:
            return qt4.QVariant(int(qt4.Qt.AlignLeft | qt4.Qt.AlignVCenter))
        if role == qt4.Qt.TextColorRole:
            if (col % 2):
                return qt4.QVariant(qt4.QColor(150, 150, 150))
            else:
                return qt4.QVariant(qt4.QColor(150, 150, 150))
        if role == qt4.Qt.BackgroundColorRole:
            if (col % 2):
                return qt4.QVariant(qt4.QColor(0, 100, 100))
            else:
                return qt4.QVariant(qt4.QColor(0, 50, 50))

    def headerData(self, section, orientation, role=qt4.Qt.DisplayRole):
        if role == qt4.Qt.TextAlignmentRole:
            return qt4.QVariant(int(qt4.Qt.AlignRight | qt4.Qt.AlignVCenter))
        if role == qt4.Qt.DisplayRole:
            if orientation == qt4.Qt.Horizontal:
                if (section % 2):
                    return qt4.QVariant("VALUE")
                else:
                    return qt4.QVariant("ADDR")

    def rowCount(self, index=qt4.QModelIndex()):
        return 16

    def columnCount(self, index=qt4.QModelIndex()):
        return 16

    def setData(self, index, value, role=qt4.Qt.EditRole):
        row = index.row()
        col = index.column()
        if index.isValid() and 0 <= index.row():
            self.registers[(col - 1) * self.rowCount() / 2 + row] = value
            return True
        return False
