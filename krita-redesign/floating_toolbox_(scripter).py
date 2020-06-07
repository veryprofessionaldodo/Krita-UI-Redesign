from krita import *
from PyQt5.QtWidgets import QWidget, QToolButton
import sys

class subWindowFilter(QObject):
    """Event Filter object"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        qWin = Application.activeWindow().qwindow()
        self.mdiArea = qWin.centralWidget().findChild(QMdiArea)
        self.target = None
        
    def eventFilter(self, obj, e):
        """Event filter: Update the Toolbox's position to match to the current view 
        if the (sub-)window has moved, changed in size or been activated."""
        if (e.type() == QEvent.Move or
            e.type() == QEvent.Resize or
            e.type() == QEvent.WindowActivate):
            self.moveToolBox()
            
        return False
        
    def moveToolBox(self):
        """Move the toolbox to the position of the current View"""
        subWin = self.mdiArea.activeSubWindow()
        if subWin and self.target:
            for c in subWin.children(): 
                if 'view' in c.objectName(): # Grab the View from the tab/sub-window
                    view = c
            
            
            ### NOTE: Determining the correct corner position might be better done based 
            ### on whether Krita is set to handle multiple documents as 'Subwindows'  or 'Tabs'
            
            # pos = self.mdiArea.pos() # Move to top of QMdiArea. Only suitable for 'Subwindows' mode.
            pos = self.mdiArea.mapFromGlobal(view.mapToGlobal(QPoint(0,0))) # Move to top left corner of current view
            self.target.move(pos)

            
            if view.height() < self.target.sizeHint().height():
                self.target.resize(self.target.sizeHint().width(), view.height())
            else:
                self.target.resize(self.target.sizeHint())
    
    def setTargetWidget(self, wdgt):
        self.target = wdgt

class floatingToolbarWidget(QWidget):
    
    def __init__(self, parent=None):
        super(floatingToolbarWidget, self).__init__(parent)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint
            )
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(4,4,4,4)
        
        self.btnHide = QToolButton()
        self.btnHide.setIcon(Application.icon("light_visible"))
        self.btnHide.setIconSize(QSize(14,14))
        self.btnHide.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.btnHide.clicked.connect(self.toggleWidgetVisible)
        self.layout().addWidget(self.btnHide)
        
        self.widget = None
        self.widgetDocker = None
        
    def closeEvent(self, e):
        self.returnDocker()
        return super().closeEvent(e)
        
    def borrowDocker(self, name):
        """Borrow a docker widget from Krita's existing list of dockers"""
        docker = Application.activeWindow().qwindow().findChild(QDockWidget, name)

        # Does requested widget exist?
        if docker and docker.widget():
            # Return any previous widget
            self.returnDocker()
                
            self.widgetDocker = docker
            self.widget = docker.widget()
            self.layout().addWidget(self.widget)    
            self.resize(self.sizeHint())        
            
            return True
            
        return False
    
    def returnDocker(self):
        """Return the borrowed docker to it's original QDockerWidget"""
        # Ensure there's a widget to return
        if self.widget:
            self.widgetDocker.setWidget(self.widget)
            self.widget = None
            self.widgetDocker = None
            
    def toggleWidgetVisible(self):
        self.widget.setVisible(not self.widget.isVisible())
        self.resize(self.sizeHint()) 

# Get all the Krita widgets we need
qWin = Application.activeWindow().qwindow()
tlbx = qWin.findChild(QDockWidget, 'ToolBox')
mdiArea = qWin.findChild(QMdiArea)

def createWidget(name, parent=None):
    wdgt = floatingToolbarWidget(parent)
    wdgt.setObjectName(name)    
    
    return wdgt

def slotMdiFilterManager(subWin):
    '''Ensure that the current SubWindow has the filter installed,
       and immediately move the Toolbox to current View.'''
    if subWin:
        subWin.installEventFilter(filterObj)
        filterObj.moveToolBox()

# Create the new floating widget
floater = createWidget('floatingToolbox', mdiArea)
floater.setStyleSheet("""
            QWidget { 
                background-color: rgba(128, 128, 128, .01);
            }
            
            .QScrollArea { 
                background-color: #00000000;
            }
            
            QScrollArea * { 
                background-color: #00000000;
            }
            
            QScrollArea QToolTip {
                background-color: #ffffff;                           
            }
            
            QAbstractButton {
                background-color: #77000000;
                border: none;
                border-radius: 4px;
            }
            
            QAbstractButton:checked {
                background-color: #aa306fa8;
            }
            
            QAbstractButton:hover {
                background-color: #1c1c1c;
            }
            
            QAbstractButton:pressed {
                background-color: #53728e;
            }
""")
floater.borrowDocker('ToolBox')

# Create and install event filter to sub window(s) and main window
filterObj = subWindowFilter() # Create filter object
filterObj.setTargetWidget(floater)
mdiArea.subWindowActivated.connect(slotMdiFilterManager)
qWin.installEventFilter(filterObj)

floater.show()