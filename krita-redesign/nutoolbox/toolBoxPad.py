from PyQt5.QtWidgets import QWidget, QToolButton, QDockWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize, QPoint

class ToolBoxPad(QWidget):

    """ An on-canvas toolbox widget. I'm dubbing widgets that 'float' 
    on top of the canvas '(lily) pads' for the time being :) """

    def __init__(self, mdiArea):
        super(ToolBoxPad, self).__init__(mdiArea)
        self.setObjectName("toolBoxPad")
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint
            )
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(4,4,4,4)

        # Members to hold a borrowed widget and it's original parent docker for returning
        self.widget = None
        self.widgetDocker = None
        
        # Visibility toggle
        self.btnHide = QToolButton()
        self.btnHide.setIcon(Application.icon("light_visible"))
        self.btnHide.setIconSize(QSize(12,12))
        self.btnHide.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.btnHide.clicked.connect(self.toggleWidgetVisible)
        self.layout().addWidget(self.btnHide)


    def closeEvent(self, e):
        """Since the plugins works by borrowing the actual docker 
        widget we need to ensure its returned upon closing the pad"""
        self.returnDocker()
        return super().closeEvent(e)


    def paintEvent(self, e):
        """Needed to prevent some ugliness and resize the Pad if 
        the user decides to change the icon size of the toolbox"""
        self.adjustToView()
        return super().paintEvent(e)


    def borrowDocker(self, docker):
        """Borrow a docker widget from Krita's existing list of dockers and 
        returns True. Returns False if invalid widget was passed. """

        # Does requested widget exist?
        if isinstance(docker, QDockWidget) and docker.widget():
            # Return any previous widget to its original docker
            self.returnDocker()
                
            self.widgetDocker = docker
            self.widget = docker.widget()
            self.layout().addWidget(self.widget) 
            self.resize(self.sizeHint())        
            
            return True
            
        return False


    def returnDocker(self):
        """Return the borrowed docker to it's original QDockWidget"""
        # Ensure there's a widget to return
        if self.widget:
            self.widgetDocker.setWidget(self.widget)
            self.widget = None
            self.widgetDocker = None


    def adjustToView(self):
        """Adjust the position and size of the Pad to that of the active View."""
        view = self.activeView()
        if view:
            # NOTE: Determining the correct corner position might be better done based 
            # on whether Krita is set to handle multiple documents as 'AdjustToSubwindows'  or 'Tabs'
            
            # pos = self.parentWidget().pos() # Move to top of QMdiArea. Only suitable for 'AdjustToSubwindows' mode.
            pos = self.parentWidget().mapFromGlobal(view.mapToGlobal(QPoint(0,0))) # Move to top left corner of current view. Hacky, but works!
            self.move(pos)

            self.resizeToView()


    def resizeToView(self):
        """Resize the Pad to an appropriate size that fits within the subwindow."""
        view = self.activeView()

        if view and self:
            if view.height() < self.sizeHint().height():
                self.resize(self.sizeHint().width(), view.height())
            else:
                self.resize(self.sizeHint())


    def activeView(self):
        """Get the View widget of the active subwindow."""
        subWin = self.parentWidget().activeSubWindow()
        
        if subWin:
            for child in subWin.children(): 
                if 'view' in child.objectName(): # Grab the View from the active tab/sub-window
                    return child


    def toggleWidgetVisible(self, value=None):

        if not value:
            value = not self.widget.isVisible()
            
        self.widget.setVisible(value)
        self.resizeToView()    