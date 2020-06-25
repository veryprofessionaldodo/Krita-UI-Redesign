from PyQt5.QtWidgets import QMdiArea, QDockWidget
from .adjustToSubwindowFilter import AdjustToSubwindowFilter
from .toolOptionsPad import ToolOptionsPad

class NuToolOptions():

    def __init__(self, window):
        qWin = window.qwindow()
        mdiArea = qWin.findChild(QMdiArea)
        toolOptions = qWin.findChild(QDockWidget, 'sharedtooldocker')

        # Create "pad"
        self.pad = ToolOptionsPad(mdiArea)
        self.pad.borrowDocker(toolOptions)
        # self.pad.setStyleSheet(self.styleSheet()) # Maybe worth tinkering with another time

        # Create and install event filter
        self.adjustFilter = AdjustToSubwindowFilter(mdiArea)
        self.adjustFilter.setTargetWidget(self.pad)
        mdiArea.subWindowActivated.connect(self.ensureFilterIsInstalled)
        qWin.installEventFilter(self.adjustFilter)

        # Create actions
        action = window.createAction("nuToolOptions", "Modern Tool Options Panel", "tools/scripts")
        action.setCheckable(True)
        action.setChecked(True)

        self.toggleAction = window.createAction("showToolOptions", "Show Tool Options", "settings")
        self.toggleAction.toggled.connect(self.pad.toggleWidgetVisible)
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
            * { 
                background-color: #00000000;
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
            
            QToolButton, QPushButton {
                background-color: #80000000;
                border: none;
                border-radius: 4px;
            }
            
            QToolButton:checked, QPushButton:checked {
                background-color: #aa306fa8;
            }
            
            QToolButton:hover, QPushButton:hover {
                background-color: #1c1c1c;
            }
            
            QToolButton:pressed, QPushButton:pressed {
                background-color: #53728e;
            }

            QAbstractSpinBox {
                background-color: #80000000;
                border: none;
                border-radius: 4px;
            }

            QComboBox {
                background-color: #80000000;
                border: none;
                border-radius: 4px;
            }

            KisSliderSpinBox {
                background-color: #80000000;
                border: none;
            }
        """
