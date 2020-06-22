from krita import *
from .adjustToSubwindowFilter import AdjustToSubwindowFilter
from .toolBoxPad import ToolBoxPad

class NuToolbox():

    def __init__(self, window):
        qWin = window.qwindow()
        mdiArea = qWin.findChild(QMdiArea)
        toolbox = qWin.findChild(QDockWidget, 'ToolBox')
        
        # Create actions
        action = window.createAction("nuToolbox", "Modern Toolbox", "tools")
        action.setCheckable(True)
        action.setChecked(True)

        # Create "pad"
        self.pad = ToolBoxPad(mdiArea)
        self.pad.borrowDocker(toolbox)
        self.pad.setStyleSheet(self.styleSheet())

        # Create and install event filter
        self.adjustFilter = AdjustToSubwindowFilter(mdiArea)
        self.adjustFilter.setTargetWidget(self.pad)
        mdiArea.subWindowActivated.connect(self.ensureFilterIsInstalled)
        qWin.installEventFilter(self.adjustFilter)


    def ensureFilterIsInstalled(self, subWin):
        """Ensure that the current SubWindow has the filter installed,
        and immediately move the Toolbox to current View."""
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
