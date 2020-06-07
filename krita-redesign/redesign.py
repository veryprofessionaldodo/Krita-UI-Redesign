from krita import *


def removeBorder(window):
    window.qwindow().setStyleSheet("""
            QToolBar {
                border: none;
            }
        """)


class Redesign(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass
        # This function could possibly be used to import a CSS file  

    def createActions(self, window):
        actions = []
        actions.append(window.createAction("toolbarBorder", "Borderless Toolbars", ""))
        actions.append(window.createAction("nuToolbox", "Transparent Toolbox", ""))
        actions.append(window.createAction("tabHeight", "Thin Document Tabs", "window"))
        actions.append(window.createAction("tabsClarity", "Enhance Tabs Clarity", "window"))

        menu = window.qwindow().menuBar().addMenu("Redesign")

        for a in actions:
            a.setCheckable(True)
            a.setChecked(True) # Activate the tweaks by default
            menu.addAction(a)

        actions[0].toggled.connect(self.toolbarBorderToggled)
        actions[1].toggled.connect(self.nuToolboxToggled)
        actions[2].toggled.connect(self.tabHeightToggled)
        actions[3].toggled.connect(self.increaseClarityToggled)

        # Remove Toolbar borders (and enhance tabs)
        
        styleSheet = """
                QToolBar {
                    border: none;
                }            

                QTabBar::tab:!selected {
                    color: gray;
                }

                QTabBar::tab:!selected:hover {
                    color: silver;
                }
            """

        # TODO: Use settings from configparser
        
        #window.qwindow().setStyleSheet(styleSheet)  
        self.setNuToolbox(window.qwindow(), True)
        self.setTabHeight(window.qwindow(), True)
        self.setToolbarsBorder(window.qwindow(), True)
        self.setIncreasedClarity(window.qwindow(), True)

        canvas = window.qwindow().centralWidget()
        canvas.setStyleSheet(styleSheet)

        toolbox = window.qwindow().findChild(QWidget, 'ToolBox')
        
        # Hides the handle at the top of the toolbox. It can still be manipulated though.
        # Maybe it's a title bar that can be disabled instead?
        # handle = toolbox.findChild(QLabel)
        # handle.setVisible(False) 
        
        # Lock the size of the toolbox. Not necessary, just my preference.
        toolbox.setFixedWidth(58) 
        toolbox.setFixedHeight(549)
        
        toolbox.setStyleSheet(styleSheet)

    def toolbarBorderToggled(self, toggled):
        self.setToolbarsBorder(Application.activeWindow().qwindow(), toggled)

    def setToolbarsBorder(self, window, toggled):
        styleSheet = """""" # Cleared by default

        if toggled:
            styleSheet = """
                QToolBar { border: none; }            
            """

        window.setStyleSheet(styleSheet)

    def increaseClarityToggled(self, toggled):
        self.setIncreasedClarity(Application.activeWindow().qwindow(), toggled)

    def setIncreasedClarity(self, window, toggled):
        styleSheet = """"""

    def tabHeightToggled(self, toggled):
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
        self.setNuToolbox( Application.activeWindow().qwindow(), toggled)


    def setNuToolbox(self, window, toggled): 
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
