from krita import *
from .adjustToSubwindowFilter import AdjustToSubwindowFilter
from .toolboxPad import ToolboxPad

class NuToolbox():

     def __init__(self):
        qWin = Application.activeWindow().qwindow()
        mdiArea = qWin.findChild(QMdiArea)

        self.pad = ToolboxPad(mdiArea)
        self.pad.setObjectName("toolBoxPad")
        self.pad.borrowDockerWidget('ToolBox')
        self.pad.setStyleSheet(self.styleSheet())

        self.adjustFilter = AdjustToSubwindowFilter()
        self.adjustFilter.setTargetWidget(self.pad)
        mdiArea.subWindowActivated.connect(self.ensureFilterIsInstalled)
        qWin.installEventFilter(self.adjustFilter)


    def ensureFilterIsInstalled(subWin):
        '''Ensure that the current SubWindow has the filter installed,
        and immediately move the Toolbox to current View.'''
        if subWin:
            subWin.installEventFilter(self.adjustFilter)
            self.adjustFilter.adjustTarget()


    def styleSheet(self):
        return """
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
        """
