from krita import *
from . import variables

class Redesign(Extension):

    usesFlatTheme = True
    usesBorderlessToolbar = True
    usesThinDocumentTabs = True
    usesTransparentToolbox = True
 
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        variables.setBackground(qApp.palette().color(QPalette.Window).name())
        variables.setAlternate(qApp.palette().color(QPalette.AlternateBase).name())
        variables.setTextColor("#b4b4b4")

        variables.buildFlatTheme()
        
        print("\n\n")
        print(variables.flat_tab_big_style)
        print("\n\n")
        
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
        
        self.rebuildStyleSheet(window.qwindow())

    def toolbarBorderToggled(self, toggled):
        Application.writeSetting("Redesign", "usesBorderlessToolbar", str(toggled).lower())

        self.usesBorderlessToolbar = toggled

        self.rebuildStyleSheet(Application.activeWindow().qwindow())


    def flatThemeToggled(self, toggled):
        Application.writeSetting("Redesign", "usesFlatTheme", str(toggled).lower())

        self.usesFlatTheme = toggled

        self.rebuildStyleSheet(Application.activeWindow().qwindow())

    
    def tabHeightToggled(self, toggled):
        Application.instance().writeSetting("Redesign", "usesThinDocumentTabs", str(toggled).lower())

        self.usesThinDocumentTabs = toggled

        self.rebuildStyleSheet(Application.activeWindow().qwindow())
        

    def nuToolboxToggled(self, toggled):
        Application.writeSetting("Redesign", "usesTransparentToolbox", str(toggled).lower())
        
        self.usesTransparentToolbox = toggled

        self.rebuildStyleSheet(Application.activeWindow().qwindow())

    def rebuildStyleSheet(self, window):
        full_style_sheet = ""

        # Full Window Changes 
        
        # Dockers
        if self.usesFlatTheme:
            full_style_sheet += "\n" + variables.flat_dock_style + "\n"
            full_style_sheet += "\n" + variables.flat_tools_style + "\n"
            full_style_sheet += "\n" + variables.flat_main_window_style + "\n"
            full_style_sheet += "\n" + variables.flat_menu_bar_style + "\n"
            full_style_sheet += "\n" + variables.flat_combo_box_style + "\n"
            full_style_sheet += "\n" + variables.flat_spin_box_style + "\n"
            full_style_sheet += "\n" + variables.flat_toolbox_style + "\n"
            full_style_sheet += "\n" + variables.flat_status_bar_style + "\n"

        # Tabs 
        if self.usesFlatTheme:
            if self.usesThinDocumentTabs:
                full_style_sheet += "\n" + variables.flat_tab_small_style + "\n"
            else: 
                full_style_sheet += "\n" + variables.flat_tab_big_style + "\n"
        else: 
            if self.usesThinDocumentTabs:
                full_style_sheet += "\n" + variables.small_tab_style + "\n"
        
        # Toolbar
        if self.usesFlatTheme:
            full_style_sheet += "\n" + variables.flat_toolbar_style + "\n"
        elif self.usesBorderlessToolbar:
            full_style_sheet += "\n" + variables.no_borders_style + "\n"
        
        window.setStyleSheet(full_style_sheet)

        # Toolbox
        toolbox = window.findChild(QWidget, 'ToolBox')
        toolbox_style = ""

        if self.usesTransparentToolbox: 
            toolbox = window.findChild(QWidget, 'ToolBox')
            toolbox_style = variables.nu_toolbox_style

            # Hides the handle at the top of the toolbox. It can still be manipulated though.
            # Maybe it's a title bar that can be disabled instead?
            # handle = toolbox.findChild(QLabel)
            # handle.setVisible(False) 

            # Lock the size of the toolbox. Not necessary, just my preference.
            toolbox.setFixedWidth(58) 
            toolbox.setFixedHeight(549)

        toolbox.setStyleSheet(toolbox_style)
        

Krita.instance().addExtension(Redesign(Krita.instance()))
