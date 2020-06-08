from PyQt5.QtWidgets import QWidget, QToolButton, QSizePolicy. QDockWidget
from PyQt5.QtCore import Qt, QSize

class ToolboxPad(QWidget):

    '''An on-canvas toolbox widget. I'm dubbing widgets that "float" 
    on top of the canvas "(lily) pads" for the time being :) '''

    def __init__(self, parent=None):
        super(ToolboxWidget, self).__init__(parent)
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
        self.btnHide.setIconSize(QSize(14,14))
        self.btnHide.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.btnHide.clicked.connect(self.toggleWidgetVisible)
        self.layout().addWidget(self.btnHide)


    def closeEvent(self, e):
        """Since the plugins works by borrowing the actual docker 
        widget we need to ensure its returned upon closing the pad"""
        self.returnDockerWidget()
        return super().closeEvent(e)
        

    def borrowDockerWidget(self, name):
        """Borrow a docker widget from Krita's existing list of dockers"""
        docker = Application.activeWindow().qwindow().findChild(QDockWidget, name)

        # Does requested widget exist?
        if docker and docker.widget():
            # Return any previous widget to its original docker
            self.returnDockerWidget()
                
            self.widgetDocker = docker
            self.widget = docker.widget()
            self.layout().addWidget(self.widget) 
            self.resize(self.sizeHint())        
            
            return True
            
        return False
    

    def returnDockerWidget(self):
        """Return the borrowed docker to it's original QDockWidget"""
        # Ensure there's a widget to return
        if self.widget:
            self.widgetDocker.setWidget(self.widget)
            self.widget = None
            self.widgetDocker = None
            

    def togglePadVisible(self):
        self.widget.setVisible(not self.widget.isVisible())
        self.resize(self.sizeHint())