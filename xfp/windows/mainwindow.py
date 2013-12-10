#!-*- coding: utf-8  -*-

from ..widgets.regtablewidget import RegTableModel
from ..widgets.panelwidget import PanelWidget
from ..widgets.controlbox import ControlBox
from .. import utils
from .. import qtall as qt4


def _(text, disambiguation=None, context='MainWindow'):
    """Translate text."""
#    return qt4.QCoreApplication.translate(context, text, disambiguation)
    return text  # do nothing

setdb = {
    'toolbar_size': 30,

}


class MainWindow(qt4.QMainWindow):
    '''table window for test xfp register'''
    def __init__(self):
        super(MainWindow, self).__init__()
        print utils.resourceDirectory
        self.resize(1440, 960)
        self.tablemodel_low = RegTableModel(self)
        self.tableview_low = qt4.QTableView()
        self.tableview_low.setModel(self.tablemodel_low)
        for i in range(32):
            self.tableview_low.setColumnWidth(i, 43)
            self.tableview_low.setRowHeight(i, 20)
        self.tablemodel_high = RegTableModel(self)
        self.tableview_high = qt4.QTableView()
        self.tableview_high.setModel(self.tablemodel_high)
        for i in range(32):
            self.tableview_high.setColumnWidth(i, 43)
            self.tableview_low.setRowHeight(i, 20)
        self.panel = PanelWidget()
        vbox = qt4.QVBoxLayout()
        vbox.addWidget(self.tableview_low)
        vbox.addWidget(self.tableview_high)
        hbox = qt4.QHBoxLayout()
        hbox.addWidget(self.panel)
        hbox.addLayout(vbox)
        self.controlbox = ControlBox(self)
        self.centralWidget = qt4.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(hbox)
        self._defineMenus()

    def _defineMenus(self):
        """Initialise the menus and toolbar"""

        #there are actions for main menu toolbars and menus
        a = utils.makeAction
        self.xfpactions = {
            'data.import':
            a(self, _('import data'), _('&Import'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'data.export':
            a(self, _('export data'), _('&Export'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'data.capture':
            a(self, _('capture data'), _('&Capture'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'help.home':
            a(self, _('help home'), _('&Help home'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'help.project':
            a(self, _('help project'), _('&Help project'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'help.bug':
            a(self, _('help bug'), _('&Help bug'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N'),
            'help.tutorial':
            a(self, _('help tutorial'), _('&Help tutorial'), self.slotFileNew,
              icon='kde-document-new', key='Ctrl+N'),
            'help.about':
            a(self, _('help about'), _('&Help about'), self.slotFileNew, icon='kde-document-new',
              key='Ctrl+N')
        }

        #create data toolbar
        tb = self.maintoolbar = qt4.QToolBar(_("data toolbar - XFP"), self)
        iconsize = setdb['toolbar_size']
        tb.setIconSize(qt4.QSize(iconsize, iconsize))
        tb.setObjectName('xfpmaintoolbar')
        self.addToolBar(qt4.Qt.TopToolBarArea, tb)
        utils.addToolbarActions(tb, self.xfpactions,
                                ('data.import', 'data.export', 'data.capture'))
        #create help toolbar
        tb = self.maintoolbar = qt4.QToolBar(_("help toolbar - XFP"), self)
        iconsize = setdb['toolbar_size']
        tb.setIconSize(qt4.QSize(iconsize, iconsize))
        tb.setObjectName('xfpmaintoolbar')
        self.addToolBar(qt4.Qt.TopToolBarArea, tb)
        utils.addToolbarActions(tb, self.xfpactions,
                                ('help.home', 'help.project', 'help.bug', 'help.tutorial',
                                 'help.about'))

        # menu structure
        cfgmenu = [
            ['cfg.uart', _('config &Uart'), []], '',
            ['cfg.pid', _('config &PID'), []], '',
        ]
        datamenu = [
            'data.import', 'data.export', '', 'data.capture'
        ]
        helpmenu = [
            'help.home', 'help.project', 'help.bug', '',
            'help.tutorial', '',
            'help.about'
        ]
        menus = [
            ['cfg', _('&config'), cfgmenu],
            ['data', _('&data'), datamenu],
            ['help', _('&help'), helpmenu]]
        self.menus = {}
        utils.constructMenus(self.menuBar(), self.menus, menus, self.xfpactions)

    def slotFileNew(self):
        """New file."""
        pass

    def slotFileSave(self):
        pass
        