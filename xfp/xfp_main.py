#!/usr/bin/env python

'''Main XFP evalution executable.'''

from __future__ import division
import sys
import os

from xfp import qtall as qt4
from xfp.windows import mainwindow
from xfp.utils import utilfuncs


def run():
    '''Run the main application.'''
    app = qt4.QApplication(sys.argv)
    resdir = utilfuncs.resourceDirectory
    #sshFile = os.path.join(resdir, "xfp/stylesheet/stylesheet.css")
    #with open(sshFile, "r") as fh:
    #    app.setStyleSheet(fh.read())
    app.setStyleSheet("QWidget { background-color: red }")
    #xfp_mainwindow = mainwindow.MainWindow()
    #xfp_mainwindow.show()
    sys.exit(app.exec_())


# if ran as a program
if __name__ == '__main__':
    run()
    