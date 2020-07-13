from PyQt5.QtWidgets import QMdiArea, QDockWidget
from .ntadjusttosubwindowfilter import ntAdjustToSubwindowFilter
from .ntwidgetpad import ntWidgetPad
from .. import variables

class ntToolBox():

    def __init__(self, window):
        qWin = window.qwindow()
        mdiArea = qWin.findChild(QMdiArea)
        toolbox = qWin.findChild(QDockWidget, 'ToolBox')

        # Create "pad"
        self.pad = ntWidgetPad(mdiArea)
        self.pad.setObjectName("toolBoxPad")
        self.pad.borrowDocker(toolbox)
        self.pad.setViewAlignment('left')
        
        # Create and install event filter
        self.adjustFilter = ntAdjustToSubwindowFilter(mdiArea)
        self.adjustFilter.setTargetWidget(self.pad)
        mdiArea.subWindowActivated.connect(self.ensureFilterIsInstalled)
        qWin.installEventFilter(self.adjustFilter)

        # Create visibility toggle action
        action = window.createAction("showToolbox", "Show Toolbox", "settings")
        action.toggled.connect(self.pad.toggleWidgetVisible)
        action.setCheckable(True)
        action.setChecked(True)

        # Disable the related QDockWidget
        self.dockerAction = self.findDockerAction(window, "Toolbox")
        self.dockerAction.setEnabled(False)


    def ensureFilterIsInstalled(self, subWin):
        """Ensure that the current SubWindow has the filter installed,
        and immediately move the Toolbox to current View."""
        if subWin:
            subWin.installEventFilter(self.adjustFilter)
            self.pad.adjustToView()
            self.updateStyleSheet()


    def findDockerAction(self, window, text):
        dockerMenu = None
        
        for m in window.qwindow().actions():
            if m.objectName() == "settings_dockers_menu":
                dockerMenu = m

                for a in dockerMenu.menu().actions():
                    if a.text().replace('&', '') == text:
                        return a
                
        return False


    def updateStyleSheet(self):
        print("Setting ToolBox")
        self.pad.setStyleSheet(variables.nu_toolbox_style)

    def close(self):
        self.dockerAction.setEnabled(True)
        return self.pad.close()