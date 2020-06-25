from PyQt5.QtWidgets import QMdiArea, QDockWidget
from .adjustToSubwindowFilter import AdjustToSubwindowFilter
from .toolBoxPad import ToolBoxPad

class NuToolbox():

    def __init__(self, window):
        qWin = window.qwindow()
        mdiArea = qWin.findChild(QMdiArea)
        toolbox = qWin.findChild(QDockWidget, 'ToolBox')

        # Create "pad"
        self.pad = ToolBoxPad(mdiArea)
        self.pad.borrowDocker(toolbox)
        self.pad.setStyleSheet(self.styleSheet())

        # Create and install event filter
        self.adjustFilter = AdjustToSubwindowFilter(mdiArea)
        self.adjustFilter.setTargetWidget(self.pad)
        mdiArea.subWindowActivated.connect(self.ensureFilterIsInstalled)
        qWin.installEventFilter(self.adjustFilter)

        # Create visibility toggle action
        action = window.createAction("showToolbox", "Show Toolbox", "settings")
        action.toggled.connect(self.pad.toggleWidgetVisible)
        action.setCheckable(True)
        action.setChecked(True)


    def ensureFilterIsInstalled(self, subWin):
        """Ensure that the current SubWindow has the filter installed,
        and immediately move the Toolbox to current View."""
        if subWin:
            subWin.installEventFilter(self.adjustFilter)
            self.pad.adjustToView()


    def styleSheet(self):
        return """
            QWidget { 
                background-color: #01808080;
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
                background-color: #70000000;
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

    def close(self):
        return self.pad.close()