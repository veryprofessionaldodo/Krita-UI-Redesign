from krita import *
from .nuTools.nttoolbox import ntToolBox
from .nuTools.nttooloptions import ntToolOptions
from . import variables
from PyQt5.QtWidgets import QMessageBox
    
class Redesign(Extension):

    usesFlatTheme = True
    usesBorderlessToolbar = True
    usesThinDocumentTabs = True
    usesNuToolbox = True
    usesNuToolOptions = True
    ntTB = None
    ntTO = None
 
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
        if Application.readSetting("", "ToolOptionsInDocker", "false") == "true":
            actions[4].setChecked(self.usesNuToolOptions)

        menu = window.qwindow().menuBar().addMenu("Redesign")

        for a in actions:
            menu.addAction(a)

        actions[0].toggled.connect(self.toolbarBorderToggled)
        actions[1].toggled.connect(self.tabHeightToggled)
        actions[2].toggled.connect(self.flatThemeToggled)
        actions[3].toggled.connect(self.nuToolboxToggled)
        actions[4].toggled.connect(self.nuToolOptionsToggled)
        
        if (self.usesNuToolOptions and
            Application.readSetting("", "ToolOptionsInDocker", "false") == "true"):
                self.ntTO = ntToolOptions(window)

        if self.usesNuToolbox: 
            self.ntTB = ntToolBox(window)

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
        Application.writeSetting("Redesign", "usesNuToolbox", str(toggled).lower())
        self.usesNuToolbox = toggled

        if toggled and not self.ntTB:
            self.ntTB = ntToolBox(Application.activeWindow())
            self.ntTB.pad.show() # This shouldn't be needed, but it is...
            self.ntTB.updateStyleSheet()
        elif not toggled and self.ntTB:
            self.ntTB.close()
            self.ntTB = None


    def nuToolOptionsToggled(self, toggled):
        if Application.readSetting("", "ToolOptionsInDocker", "false") == "true":
            Application.writeSetting("Redesign", "usesNuToolOptions", str(toggled).lower())
            self.usesNuToolOptions = toggled

            if toggled and not self.ntTO:
                self.ntTO = ntToolOptions(Application.activeWindow())
                self.ntTO.pad.show() # This shouldn't be needed, but it is..
                self.ntTO.updateStyleSheet()
            elif not toggled and self.ntTO:
                self.ntTO.close()
                self.ntTO = None
        else:
            msg = QMessageBox()
            msg.setText("nuTools requires the Tool Options Location to be set to 'In Docker'. \n\n" +
                        "This setting can be found at Settings -> Configure Krita... -> General -> Tools -> Tool Options Location." +
                        "Once the setting has been changed, please restart Krita.")
            msg.exec_()


    def rebuildStyleSheet(self, window):
        full_style_sheet = ""
        
        # Dockers
        if self.usesFlatTheme:
            full_style_sheet += f"\n {variables.flat_dock_style} \n"
            full_style_sheet += f"\n {variables.flat_tools_style} \n"
            full_style_sheet += f"\n {variables.flat_main_window_style} \n"
            full_style_sheet += f"\n {variables.flat_menu_bar_style} \n"
            full_style_sheet += f"\n {variables.flat_combo_box_style} \n"
            full_style_sheet += f"\n {variables.flat_spin_box_style} \n"
            full_style_sheet += f"\n {variables.flat_status_bar_style} \n"
            full_style_sheet += f"\n {variables.flat_tab_base_style} \n"
            full_style_sheet += f"\n {variables.flat_tree_view_style} \n"
            full_style_sheet += f"\n {variables.flat_tab_base_style} \n"

        # Toolbar
        if self.usesFlatTheme:
            full_style_sheet += f"\n {variables.flat_toolbar_style} \n"
        elif self.usesBorderlessToolbar:
            full_style_sheet += f"\n {variables.no_borders_style} \n"    
        
        window.setStyleSheet(full_style_sheet)

        print("\n\n")
        print(full_style_sheet)
        print("\n\n")

        # Overview
        overview = window.findChild(QWidget, 'OverviewDocker')
        overview_style = ""

        if self.usesFlatTheme:
            overview_style += f"\n {variables.flat_overview_docker_style} \n"

        overview.setStyleSheet(overview_style)

        # For document tab
        canvas_style_sheet = ""

        if self.usesFlatTheme:
            if self.usesThinDocumentTabs:
                canvas_style_sheet += f"\n {variables.flat_tab_small_style} \n"
            else: 
                canvas_style_sheet += f"\n {variables.flat_tab_big_style} \n"
        else: 
            if self.usesThinDocumentTabs:
                canvas_style_sheet += f"\n {variables.small_tab_style} \n"

        canvas = window.centralWidget()
        canvas.setStyleSheet(canvas_style_sheet)

        # This is ugly, but it's the least ugly way I can get the canvas to 
        # update it's size (for now)
        canvas.resize(canvas.sizeHint())

        # Update Tool Options stylesheet
        if self.usesNuToolOptions and self.ntTO:
            self.ntTO.updateStyleSheet()

        # Update Toolbox stylesheet
        if self.usesNuToolbox and self.ntTB:
            self.ntTB.updateStyleSheet()  

Krita.instance().addExtension(Redesign(Krita.instance()))
