from PyQt5.QtWidgets import QWidget, QLayout, QToolButton, QDockWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize, QPoint

from PyQt5.QtWidgets import QMessageBox
def boop(text): # Print a message to a dialog box
    msg = QMessageBox()
    msg.setText(str(text))
    msg.exec_()

class ToolOptionsContainer(QWidget):

    def __init__(self, parent=None):
        super(ToolOptionsContainer, self).__init__(parent)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)


class ToolOptionsPad(QWidget):

    """ An on-canvas toolbox widget. I'm dubbing widgets that 'float' 
    on top of the canvas '(lily) pads' for the time being :) """

    def __init__(self, mdiArea):
        super(ToolOptionsPad, self).__init__(mdiArea)
        self.setObjectName("toolOptionsPad")
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint
            )
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(4,4,4,4)

        # Members to hold a borrowed widget and it's original parent docker for returning
        self.widget = None
        self.widgetDocker = None
        self.container = ToolOptionsContainer()
        
        # Visibility toggle
        self.btnHide = QToolButton()
        self.btnHide.setIcon(Application.icon("light_visible"))
        self.btnHide.setIconSize(QSize(12,12))
        self.btnHide.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.btnHide.clicked.connect(self.toggleWidgetVisible)
        self.btnHide.setStyleSheet("""
            QToolButton {
                background-color: #80000000;
                border: none;
                border-radius: 4px;
            }
            
            QToolButton:checked {
                background-color: #aa306fa8;
            }
            
            QToolButton:hover {
                background-color: #1c1c1c;
            }
            
            QToolButton:pressed {
                background-color: #53728e;
            }
            """)

        self.layout().addWidget(self.btnHide)#, 0, Qt.AlignRight)


    def closeEvent(self, e):
        """Since the plugins works by borrowing the actual docker 
        widget we need to ensure its returned upon closing the pad"""
        self.returnDocker()
        return super().closeEvent(e)


    def paintEvent(self, e):
        """Needed to resize the Pad if the user decides to 
        change the icon size of the toolbox"""
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

            # Because I'm forced to use "setFixedSize" to resize the tool options
            # it needs to be put in a container, otherwise it's going to break if/when
            # returned to its original docker. Manipulate the container; not the widget.
            self.container = ToolOptionsContainer()
            self.container.layout().addWidget(self.widget)

            self.layout().addWidget(self.container, 0, Qt.AlignRight) 
            self.adjustToView()        
            
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
            
            self.resizeToView() # Resize first because the x-position is dependant on correct width.

            # pos = self.parentWidget().mapFromGlobal(view.mapToGlobal(QPoint(view.width() - self.parentWidget().width(), 0))) # Move to top of QMdiArea. Only suitable for 'AdjustToSubwindows' mode.
            pos = self.parentWidget().mapFromGlobal(view.mapToGlobal(QPoint(view.width() - self.width(), 0))) # Move to top left corner of current view. Hacky, but works!
            self.move(pos)
    
    def resizeToView(self): # The Tool Options widget is a nightmare to resize :)
        """Resize the Pad to an appropriate size that fits within the subwindow."""
        view = self.activeView()

        if view and self.widget.isVisible():
            # We start with the tool options sizeHint as a goal size and then
            # shrink it down if necessary to fit inside the view.
            containerSize = self.widget.widget().sizeHint()

            # I don't like all these magic numbers (And repeteition) but I honestly don't know what they
            # correspond to either. Margins, I suppose, but then why is one of the numbers 14
            # when the margins are all 4?

            if view.height() < containerSize.height() + self.btnHide.height() + 14:
                containerSize.setHeight(view.height() - self.btnHide.height() - 14)

            if view.width() < containerSize.width() + 8:
                containerSize.setWidth(view.width() - 8)
            
            self.container.setFixedSize(containerSize)

            # Once the tool options container is an appropriate size, resize the
            # Pad widget to it's appropriate sizes
            padSize = self.sizeHint()
            if view.height() < padSize.height():
                padSize.setHeight(view.height())

            if view.width() < padSize.width():
                padSize.setWidth(view.width())
            
            self.setFixedSize(padSize)

        elif not self.widget.isVisible():
            # Resize the widget to the size of the button + some extra height for the hidden widget I guess?

            # I just don't know what these numbers are, or why I can't use the 
            # button's own sizeHint. The result also varies if something else
            # about the layout varies.
            self.setFixedSize(23, 54) 


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