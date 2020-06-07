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
<<<<<<< HEAD
        removeBorder(window)


Krita.instance().addExtension(Redesign(Krita.instance()))
=======
        actions = []
        actions.append(window.createAction("toolbarBorder", "Borderless toolbars", ""))
        actions.append(window.createAction("nuToolbox", "Transparent toolbox", ""))
        actions.append(window.createAction("tabHeight", "Thin document tabs", "window"))
        menu = window.qwindow().menuBar().addMenu("Redesign")

        for a in actions:
            a.setCheckable(True)
            a.setChecked(True) # Activate the tweaks by default
            menu.addAction(a)
        
        actions[0].toggled.connect(self.toolbarBorderToggled)
        actions[1].toggled.connect(self.nuToolboxToggled)
        actions[2].toggled.connect(self.tabHeightToggled)

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

        window.qwindow().setStyleSheet(styleSheet)
        
        # Tab height
        styleSheet = """
                QTabBar::tab { height: 23px; }
            """

        canvas = window.qwindow().centralWidget()
        canvas.setStyleSheet(styleSheet)

        # Transparent Toolbox
        styleSheet = """

            KoToolBoxDocker { 
                background-color: rgba(128, 128, 128, .01);
                margin: 2px; 
            }
            
            .KoToolBoxScrollArea { 
                background-color: #00000000;
            }
            
            KoToolBoxScrollArea * { 
                background-color: #00000000;
            }
            
            KoToolBoxDocker QLabel {
                border: none;
                border-radius: 4px; 
                background-color: #77000000;
            }
            
            KoToolBoxScrollArea QToolTip {
                background-color: #ffffff;                           
            }
            
            KoToolBoxButton {
                background-color: #77000000;
                border: none;
                border-radius: 4px;
                margin-right: 1px;
                margin-top: 1px;
            }
            
            KoToolBoxButton:checked {
                background-color: #aa306fa8;
            }
            
            KoToolBoxButton:hover {
                background-color: #1c1c1c;
            }
            
            KoToolBoxButton:pressed {
                background-color: #53728e;
            }
            
        """

        toolbox = window.qwindow().findChild(QWidget, 'ToolBox')
        
        # Hides the handle at the top of the toolbox. It can still be manipulated though.
        # Maybe it's a title bar that can be disabled instead?
        # handle = toolbox.findChild(QLabel)
        # handle.setVisible(False) 
        
        # Lock the size of the toolbox. Not necessary, just my preference.
        toolbox.setFixedWidth(58) 
        toolbox.setFixedHeight(549)
        
        toolbox.setStyleSheet(styleSheet)


    """ Becuse Krita loads the main window in a very... curious way 
    the functions below can't be used in 'createActions()'. This is
    why the code of the functions are ran separately in 'createActions()'.
    We need to use the 'window' argument of 'createActions()' to
    set the style sheets immediately on launch. I'm not sure if theres
    a way to maybe pass a 'window' argument to these function?"""


    def toolbarBorderToggled(self, toggled):
        styleSheet = """""" # Cleared by default

        if toggled:
            styleSheet = """
                QToolBar { border: none; }            
            """

        Application.activeWindow().qwindow().setStyleSheet(styleSheet)


    def tabHeightToggled(self, toggled):
        styleSheet = """""" # Clear by default

        if toggled:
            styleSheet = """
                QTabBar::tab { height: 23px; }
            """
            
        canvas = Application.activeWindow().qwindow().centralWidget()
        canvas.setStyleSheet(styleSheet)

        # This is ugly, but it's the least ugly way I can get the canvas to 
        # update it's size (for now)
        canvas.resize(canvas.sizeHint())


    def nuToolboxToggled(self, toggled):
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

        toolbox = Application.activeWindow().qwindow().findChild(QWidget, 'ToolBox')

         # Hides the handle at the top of the toolbox. It can still be manipulated though.
        # Maybe it's a title bar that can be disabled instead?
        # handle = toolbox.findChild(QLabel)
        # handle.setVisible(False) 
        
        # Lock the size of the toolbox. Not necessary, just my preference.
        toolbox.setFixedWidth(58) 
        toolbox.setFixedHeight(549)

        toolbox.setStyleSheet(styleSheet)
        
Krita.instance().addExtension(Redesign(Krita.instance()))
>>>>>>> 73d29bfe6870aa4e24266d0b74de8b1313f388d9
