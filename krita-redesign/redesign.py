from krita import *
from .nutoolbox.nutoolbox import NuToolbox
from .nutooloptions.nutooloptions import NuToolOptions
from . import variables

class Redesign(Extension):

    usesFlatTheme = True
    usesBorderlessToolbar = True
    usesThinDocumentTabs = True
    usesNuToolbox = True
    usesNuToolOptions = True
    nuTb = None
    nuTO = None
 
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        variables.setBackground(qApp.palette().color(QPalette.Window).name())
        variables.setAlternate(qApp.palette().color(QPalette.AlternateBase).name())
        variables.setTextColor("#b4b4b4")

        variables.buildFlatTheme()
        
        if Application.readSetting("Redesign", "usesFlatTheme", "false") == "false":
            self.usesFlatTheme = False

        if Application.readSetting("Redesign", "usesBorderlessToolbar", "false") == "false":
            self.usesBorderlessToolbar = False

        if Application.readSetting("Redesign", "usesThinDocumentTabs", "false") == "false":
            self.usesThinDocumentTabs = False

        if Application.readSetting("Redesign", "usesNuToolbox", "false") == "false":
            self.usesNuToolbox = False
        
        if Application.readSetting("Redesign", "usesNuToolOptions", "false") == "false":
            self.usesNuToolOptions = False


    def createActions(self, window):
        actions = []

        actions.append(window.createAction("toolbarBorder", "Borderless Toolbars", ""))
        actions[0].setCheckable(True)
        actions[0].setChecked(self.usesBorderlessToolbar) 

        actions.append(window.createAction("tabHeight", "Thin Document Tabs", ""))
        actions[1].setCheckable(True)
        actions[1].setChecked(self.usesThinDocumentTabs)

        actions.append(window.createAction("flatTheme", "Use flat theme", ""))
        actions[2].setCheckable(True)
        actions[2].setChecked(self.usesFlatTheme)

        actions.append(window.createAction("nuToolbox", "NuToolbox", ""))
        actions[3].setCheckable(True)
        actions[3].setChecked(self.usesNuToolbox)

        actions.append(window.createAction("nuToolOptions", "NuToolOptions", ""))
        actions[4].setCheckable(True)
        actions[4].setChecked(self.usesNuToolOptions)

        menu = window.qwindow().menuBar().addMenu("Redesign")

        for a in actions:
            menu.addAction(a)

        actions[0].toggled.connect(self.toolbarBorderToggled)
        actions[1].toggled.connect(self.tabHeightToggled)
        actions[2].toggled.connect(self.flatThemeToggled)
        actions[3].toggled.connect(self.nuToolboxToggled)
        actions[4].toggled.connect(self.nuToolOptionsToggled)
        
        self.rebuildStyleSheet(window.qwindow())

        if self.usesNuToolbox: 
            self.nuTb = NuToolbox(window)
            
        if self.usesNuToolOptions: 
            self.nuTO = NuToolOptions(window)


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
        Application.writeSetting("Redesign", "usesNuToolbox", str(toggled).lower())

        self.usesNuToolbox = toggled

        if toggled and not self.nuTb:
            self.nuTb = NuToolbox(Application.activeWindow())
            self.nuTb.pad.show() # This shouldn't be needed, but it is...
        elif not toggled and self.nuTb:
            self.nuTb.close()
            self.nuTb = None


    def nuToolOptionsToggled(self, toggled):
        Application.writeSetting("Redesign", "usesNuToolOptions", str(toggled).lower())

        self.usesNuToolOptions = toggled

        if toggled and not self.nuTO:
            self.nuTO = NuToolOptions(Application.activeWindow())
            self.nuTO.pad.show()
        elif not toggled and self.nuTO:
            self.nuTO.close()
            self.nuTO = None


    def rebuildStyleSheet(self, window):
        full_style_sheet = ""

        # Full Window Changes 
        
        # Dockers
        if self.usesFlatTheme:
            full_style_sheet += f"\n {variables.flat_dock_style} \n"
            full_style_sheet += f"\n {variables.flat_tools_style} \n"
            full_style_sheet += f"\n {variables.flat_main_window_style} \n"
            full_style_sheet += f"\n {variables.flat_menu_bar_style} \n"
            full_style_sheet += f"\n {variables.flat_combo_box_style} \n"
            full_style_sheet += f"\n {variables.flat_spin_box_style} \n"
            full_style_sheet += f"\n {variables.flat_toolbox_style} \n"
            full_style_sheet += f"\n {variables.flat_status_bar_style} \n"

        # Tabs 
        if self.usesFlatTheme:
            if self.usesThinDocumentTabs:
                full_style_sheet += f"\n {variables.flat_tab_small_style} \n"
            else: 
                full_style_sheet += f"\n {variables.flat_tab_big_style} \n"
        else: 
            if self.usesThinDocumentTabs:
                full_style_sheet += f"\n {variables.small_tab_style} \n"
        
        # Toolbar
        if self.usesFlatTheme:
            full_style_sheet += f"\n {variables.flat_toolbar_style} \n"
        elif self.usesBorderlessToolbar:
            full_style_sheet += f"\n {variables.no_borders_style} \n"
        
        window.setStyleSheet(full_style_sheet)
        

Krita.instance().addExtension(Redesign(Krita.instance()))
