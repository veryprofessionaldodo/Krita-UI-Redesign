"""
    Plugin for Krita UI Redesign, Copyright (C) 2020 Kapyia, Pedro Reis

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from PyQt5.QtWidgets import QWidget, QToolButton, QDockWidget, QVBoxLayout, QSizePolicy, QScrollArea
from PyQt5.QtCore import Qt, QSize, QPoint
from .ntscrollareacontainer import ntScrollAreaContainer
from .nttogglevisiblebutton import ntToggleVisibleButton
from krita import Krita

class ntWidgetPad(QWidget):
    """
    An on-canvas toolbox widget. I'm dubbing widgets that 'float' 
    on top of the canvas '(lily) pads' for the time being :) """

    def __init__(self, parent):
        super(ntWidgetPad, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint
            )
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(4,4,4,4)
        self.alignment = 'left'

        # Members to hold a borrowed widget and it's original parent docker for returning
        self.widget = None
        self.widgetDocker = None

         # Visibility toggle
        self.btnHide = ntToggleVisibleButton()
        self.btnHide.clicked.connect(self.toggleWidgetVisible)
        self.layout().addWidget(self.btnHide)

    def activeView(self):
        """
        Get the View widget of the active subwindow."""
        if not self.parentWidget():
            return None 
        
        subWin = self.parentWidget().activeSubWindow()
        
        if not subWin:
            return None

        for child in subWin.children(): 
            if 'view' in child.objectName(): # Grab the View from the active tab/sub-window
                return child
        
        return None


    def adjustToView(self):
        """
        Adjust the position and size of the Pad to that of the active View."""
        view = self.activeView()
        if view:            
            self.resizeToView()

            globalTargetPos = QPoint()
            if self.alignment == 'left':
                globalTargetPos = view.mapToGlobal(QPoint(self.rulerMargin(), 0))
            elif self.alignment == 'right':
                globalTargetPos = view.mapToGlobal(QPoint(view.width() - self.width() - self.scrollBarMargin(), 0))

            self.move(self.parentWidget().mapFromGlobal(globalTargetPos))


    def borrowDocker(self, docker):
        """
        Borrow a docker widget from Krita's existing list of dockers and 
        returns True. Returns False if invalid widget was passed."""

        # Does requested widget exist?
        if isinstance(docker, QDockWidget) and docker.widget():
            # Return any previous widget to its original docker
            self.returnDocker()
           
            self.widgetDocker = docker

            if isinstance(docker.widget(), QScrollArea):
                self.widget = ntScrollAreaContainer(docker.widget())
            else:
                self.widget = docker.widget()

            self.layout().addWidget(self.widget) 
            self.adjustToView()        
            self.widgetDocker.hide()

            return True
            
        return False


    def closeEvent(self, e):
        """
        Since the plugins works by borrowing the actual docker 
        widget we need to ensure its returned upon closing the pad"""
        self.returnDocker()
        return super().closeEvent(e)


    def paintEvent(self, e):
        """
        Needed to resize the Pad if the user decides to 
        change the icon size of the toolbox"""
        self.adjustToView()
        return super().paintEvent(e)


    def resizeToView(self):
        """
        Resize the Pad to an appropriate size that fits within the subwindow."""
        view = self.activeView()

        if view:
            
            ### GOAL: REMOVE THIS IF-STATEMENT
            if isinstance(self.widget, ntScrollAreaContainer):
                containerSize = self.widget.sizeHint() 
                
                if view.height() < containerSize.height() + self.btnHide.height() + 14 + self.scrollBarMargin():
                    containerSize.setHeight(view.height() - self.btnHide.height() - 14 - self.scrollBarMargin())

                if view.width() < containerSize.width() + 8 + self.scrollBarMargin():
                    containerSize.setWidth(view.width() - 8 - self.scrollBarMargin())
                
                self.widget.setFixedSize(containerSize)


            newSize = self.sizeHint()
            if view.height() < newSize.height():
                newSize.setHeight(view.height())

            if view.width() < newSize.width():
                newSize.setWidth(view.width())
            
            self.resize(newSize)


    def returnDocker(self):
        """
        Return the borrowed docker to it's original QDockWidget"""
        # Ensure there's a widget to return
        if self.widget:
            if isinstance(self.widget, ntScrollAreaContainer):
                self.widgetDocker.setWidget(self.widget.scrollArea())
            else:
                self.widgetDocker.setWidget(self.widget)

            self.widgetDocker.show()
            self.widget = None
            self.widgetDocker = None


    def rulerMargin(self):
        if Krita.instance().readSetting("", 'showrulers', "true") == "true":
            return 20 # Canvas ruler pixel width on Windows
        return 0


    def scrollBarMargin(self):
        if Krita.instance().readSetting("", "hideScrollbars", "false") == "true":
            return 0

        return 14 # Canvas crollbar pixel width/height on Windows 


    def setViewAlignment(self, newAlignment):
        """
        Set the Pad's alignment to the view to either 'left' or 'right'. 
        Returns False if the argument is an invalid value."""
        if isinstance(newAlignment, str):
            if (newAlignment.lower() == 'left' or
                newAlignment.lower() == 'right'):
                self.alignment = newAlignment.lower()

                self.btnHide.setArrow(self.alignment)

                return True
    
        return False


    def toggleWidgetVisible(self, value=None):
        if not value:
            value = not self.widget.isVisible()
        
        self.widget.setVisible(value)
        self.adjustToView()  
        self.updateHideButtonIcon(value)


    def updateHideButtonIcon(self, isVisible): 
        """
        Flip the direction of the arrow to fit the Pads current visibility"""
        if self.alignment == 'left':
            if isVisible:
                self.btnHide.setArrowType(Qt.ArrowType.LeftArrow)
            else:
                self.btnHide.setArrowType(Qt.ArrowType.RightArrow)
        elif self.alignment == 'right':
            if isVisible:
                self.btnHide.setArrowType(Qt.ArrowType.RightArrow)
            else:
                self.btnHide.setArrowType(Qt.ArrowType.LeftArrow)

    def getViewAlignment(self):
        return self.alignment
