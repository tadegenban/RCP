#!-*- coding: utf-8  -*-

from __future__ import division
from . import utilfuncs
import os.path
import textwrap
from .. import qtall as qt4

# where images are stored
imagedir = os.path.join(utilfuncs.resourceDirectory, 'icons/veusz')
_pixmapcache = {}
def getPixmap(pixmap):
    """Return a cached QPixmap for the filename in the icons directory."""
    if pixmap not in _pixmapcache:
        _pixmapcache[pixmap] = qt4.QPixmap(os.path.join(imagedir, pixmap))
    return _pixmapcache[pixmap]

def pixmapExists(pixmap):
    """Does the pixmap exist?"""
    return (pixmap in _pixmapcache or
            os.path.exists(os.path.join(imagedir, pixmap)))

_iconcache = {}
def getIcon(icon):
    """Return a cached QIconSet for the filename in the icons directory."""
    if icon not in _iconcache:
        svg = os.path.join(imagedir, icon+'.svg')
        if os.path.exists(svg):
            filename = svg
        else:
            filename = os.path.join(imagedir, icon+'.png')

        _iconcache[icon] = qt4.QIcon(filename)
    return _iconcache[icon]

def makeAction(parent, descr, menutext, slot, icon=None, key=None,
               checkable=False):
    """A quick way to set up an QAction object."""
    a = qt4.QAction(parent)
    a.setText(menutext)
    a.setStatusTip(descr)
    a.setToolTip(textwrap.fill(descr, 25))
    if slot:
        parent.connect(a, qt4.SIGNAL('triggered()'), slot)
    if icon:
        a.setIcon(getIcon(icon))
    if key:
        a.setShortcut( qt4.QKeySequence(key) )
    if checkable:
        a.setCheckable(True)
    return a

def addToolbarActions(toolbar, actions, which):
    """Add actions listed in "which" from dict "actions" to toolbar "toolbar".
    """
    for w in which:
        toolbar.addAction(actions[w])

def constructMenus(rootobject, menuout, menutree, actions):
    """Add menus to the output dict from the tree, listing actions
    from actions.

    rootobject: QMenu or QMenuBar to add menus to
    menuout: dict to store menus
    menutree: tree structure to create menus from
    actions: dict of actions to assign to menu items
    """

    for menuid, menutext, actlist in menutree:
        # make a new menu if necessary
        if menuid not in menuout:
            menu = rootobject.addMenu(menutext)
            menuout[menuid] = menu
        else:
            menu = menuout[menuid]

        # add actions to the menu
        for action in actlist:
            if utilfuncs.isiternostr(action):
                # recurse for submenus
                constructMenus(menu, menuout, [action], actions)
            elif action == '':
                # blank means separator
                menu.addSeparator()
            else:
                # normal action
                menu.addAction(actions[action])

def populateMenuToolbars(items, toolbar, menus):
    """Construct the menus and toolbar from the list of items.
    toolbar is a QToolbar object
    menus is a dict of menus to add to

    Items are tuples consisting of:
    (actioname, status bar text, menu text, menu id, slot,
     icon filename, add to toolbar (bool), shortcut text)

    Returns a dict of actions
    """

    actions = {}
    parent = toolbar.parent()
    for i in items:
        if len(i) == 1:
            if menus is not None:
                menus[i[0]].addSeparator()
            continue
        
        menuid, descr, menutext, menu, slot, icon, addtool, key = i

        # create action
        action = qt4.QAction(parent)
        action.setText(menutext)
        action.setStatusTip(descr)
        action.setToolTip(descr)

        # set shortcut if set
        if key:
            action.setShortcut( qt4.QKeySequence(key) )

        # load icon if set
        if icon:
            action.setIcon(getIcon(icon))

        if callable(slot):
            # connect the action to the slot
            if slot is not None:
                qt4.QObject.connect( action, qt4.SIGNAL('triggered()'), slot )
                # add to menu
            if menus is not None:
                menus[menu].addAction(action)
        elif slot is not None:
            if menus is not None:
                submenu = menus[menu].addMenu(menutext)
                menus["%s.%s"%(menu ,menuid)] = submenu
                populateMenuToolbars(slot, toolbar, menus)
        else:
            if menus is not None:
                menus[menu].addAction(action)

        # add to toolbar
        if addtool and toolbar is not None:
            toolbar.addAction(action)

        # save for later
        actions[menuid] = action

    return actions
