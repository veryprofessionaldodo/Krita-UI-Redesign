from krita import *

def removeBorder(window):
    window.qwindow().setStyleSheet("""
            QToolBar {
                border: none;
            }
        """)

class Redesign(Extension):

    usesFlatTheme = True
    usesBorderlessToolbar = True
    usesThinDocumentTabs = True
    usesTransparentToolbox = True
 
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        if Application.readSetting("Redesign", "usesFlatTheme", "false") == "false":
            self.usesFlatTheme = False

        if Application.readSetting("Redesign", "usesBorderlessToolbar", "false") == "false":
            self.usesBorderlessToolbar = False

        if Application.readSetting("Redesign", "usesThinDocumentTabs", "false") == "false":
            self.usesThinDocumentTabs = False

        if Application.readSetting("Redesign", "usesTransparentToolbox", "false") == "false":
            self.usesTransparentToolbox = False
        

    def createActions(self, window):
        actions = []

        actions.append(window.createAction("toolbarBorder", "Borderless Toolbars", ""))
        actions[0].setCheckable(True)
        actions[0].setChecked(self.usesBorderlessToolbar) 

        actions.append(window.createAction("nuToolbox", "Transparent Toolbox", ""))
        actions[1].setCheckable(True)
        actions[1].setChecked(self.usesTransparentToolbox)

        actions.append(window.createAction("tabHeight", "Thin Document Tabs", "window"))
        actions[2].setCheckable(True)
        actions[2].setChecked(self.usesThinDocumentTabs)

        actions.append(window.createAction("flatTheme", "Use flat theme", "window"))
        actions[3].setCheckable(True)
        actions[3].setChecked(self.usesFlatTheme)

        menu = window.qwindow().menuBar().addMenu("Redesign")

        for a in actions:
            menu.addAction(a)

        actions[0].toggled.connect(self.toolbarBorderToggled)
        actions[1].toggled.connect(self.nuToolboxToggled)
        actions[2].toggled.connect(self.tabHeightToggled)
        actions[3].toggled.connect(self.flatThemeToggled)
        
        if self.usesBorderlessToolbar:
            self.setToolbarsBorder(window.qwindow(), True)
        
        if self.usesTransparentToolbox:
            self.setNuToolbox(window.qwindow(), True)
        
        if self.usesThinDocumentTabs:
            self.setTabHeight(window.qwindow(), True)
        
        if self.usesFlatTheme:
            self.setFlatTheme(window.qwindow(), True)

    def toolbarBorderToggled(self, toggled):
        Application.writeSetting("Redesign", "usesBorderlessToolbar", str(toggled).lower())
        self.setToolbarsBorder(Application.activeWindow().qwindow(), toggled)

    def setToolbarsBorder(self, window, toggled):
        styleSheet = """""" # Cleared by default

        if toggled:
            styleSheet = """
                QToolBar { border: none; }            
            """

        window.setStyleSheet(styleSheet)

    def flatThemeToggled(self, toggled):
        Application.writeSetting("Redesign", "usesFlatTheme", str(toggled).lower())
        self.setFlatTheme(Application.activeWindow().qwindow(), toggled)

    def setFlatTheme(self, window, toggled):
        styleSheet = """"""

    def tabHeightToggled(self, toggled):
        Application.instance().writeSetting("Redesign", "usesThinDocumentTabs", str(toggled).lower())
        self.setTabHeight(Application.activeWindow().qwindow(), toggled)
        
    def setTabHeight(self, window, toggled):
        styleSheet = """""" # Clear by default

        if toggled:
            styleSheet = """
                QTabBar::tab { height: 23px; }
            """
            
        canvas = window.centralWidget()
        canvas.setStyleSheet(styleSheet)

        # This is ugly, but it's the least ugly way I can get the canvas to 
        # update it's size (for now)
        canvas.resize(canvas.sizeHint())

    def nuToolboxToggled(self, toggled):
        Application.writeSetting("Redesign", "usesTransparentToolbox", str(toggled).lower())
        self.setNuToolbox( Application.activeWindow().qwindow(), toggled)

    def setNuToolbox(self, window, toggled): 
        toolbox = window.findChild(QWidget, 'ToolBox')
        
        # Hides the handle at the top of the toolbox. It can still be manipulated though.
        # Maybe it's a title bar that can be disabled instead?
        # handle = toolbox.findChild(QLabel)
        # handle.setVisible(False) 
        
        # Lock the size of the toolbox. Not necessary, just my preference.
        toolbox.setFixedWidth(58) 
        toolbox.setFixedHeight(549)
        
        styleSheet = """""" # Clear by default

        if toggled:
            styleSheet = """

            KoToolBoxDocker { 
                background-color: rgba(128, 128, 128, .01);
                margin: 2px; 
            }
            
            .KoToolBoxScrollArea { 
                background-color: rgba(0,0,0,0);
            }
            
            KoToolBoxScrollArea * { 
                background-color: rgba(0,0,0,0);
            }
            
            KoToolBoxDocker QLabel {
                border: none;
                border-radius: 3px; 
                background-color: #66000000;
            }
            
            KoToolBoxScrollArea QToolTip {
                background-color: #ffffff;                           
            }
            
            KoToolBoxButton {
                background-color: #66000000;
                border: none;
                border-radius: 3px;
                margin-right: 1px;
                margin-top: 1px;
            }
            
            KoToolBoxButton:checked {
                background-color: #aa306fa8;
            }
            
            KoToolBoxButton:hover {
                background-color: inherit;
            }
            
            KoToolBoxButton:pressed {
                background-color: #53728e;
            }
            
        """

        toolbox = window.findChild(QWidget, 'ToolBox')

         # Hides the handle at the top of the toolbox. It can still be manipulated though.
        # Maybe it's a title bar that can be disabled instead?
        # handle = toolbox.findChild(QLabel)
        # handle.setVisible(False) 
        
        # Lock the size of the toolbox. Not necessary, just my preference.
        toolbox.setFixedWidth(58) 
        toolbox.setFixedHeight(549)

        toolbox.setStyleSheet(styleSheet)
        
Krita.instance().addExtension(Redesign(Krita.instance()))
