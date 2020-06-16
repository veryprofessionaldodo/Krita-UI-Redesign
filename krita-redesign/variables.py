background = "black"
alternate = "black"
tab_text_color = "#b4b4b4"

no_borders_style = " QToolBar { border: none; } "
nu_toolbox_style = """

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
            }"""
small_tab_style = "QTabBar::tab { height: 23px; }"

flat_tab_base_style = ""
flat_tab_big_style = ""
flat_tab_small_style = ""
flat_main_window_style = ""
flat_tools_style = ""
flat_dock_style = ""
flat_toolbar_style = ""
flat_menu_bar_style = ""
flat_combo_box_style = ""
flat_spin_box_style = ""
flat_toolbox_style = ""
flat_status_bar_style = ""
flat_tree_view_style = ""

def buildFlatTheme():
    global flat_tab_base_style
    global flat_tab_big_style
    global flat_tab_small_style
    global flat_main_window_style
    global flat_tools_style
    global flat_dock_style
    global flat_toolbar_style
    global flat_menu_bar_style
    global flat_combo_box_style
    global flat_spin_box_style
    global flat_toolbox_style
    global flat_status_bar_style
    global flat_tree_view_style
    
    flat_tab_base_style = f""" 
        QTabBar {{
            background-color: {background};
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
        }}
    
       QTabBar::tab:!selected {{
           background-color: {alternate};
           color: {tab_text_color};
       }}

       QTabBar::tab:only-one {{
           margin: 0px;
       }}

       QTabBar::tab:hover {{
           color: white;
       }}
       """ 
    flat_tab_big_style = f"""QTabBar::tab {{
            background-color: {background};
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
            padding: 8px;
        }}"""
    flat_tab_small_style = f""" 
        QTabBar::tab {{
            background-color: {background};
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
            height: 23px;
            padding: 8px;
        }}"""

    flat_main_window_style = f"""KisMainWindow {{
            background-color: {background};
        }} 

        KisMainWindow::separator {{
            height: 0px;
        }}"""
    flat_tools_style = f"""QToolButton, QPushButton {{
            background-color: {background};
            border-radius: 4px;
        }}

        QToolButton:hover, QPushButton:hover {{
            border: none;
            background-color: {alternate};
        }}

        QToolButton[popupMode="1"] {{
            padding-right: 13px;
        }}

        QToolButton::menu-button {{
            border: none;
            border-radius: 4px;
        }}"""
    flat_dock_style = f""" QDockWidget {{
            titlebar-close-icon: url(:/16_dark_tab-close.svg);
            titlebar-normal-icon: url(:/light_duplicatelayer.svg);
            border-bottom-right-radius: 4px;
            border-bottom-left-radius: 4px;
        }}

        QDockWidget::close-button {{
            border: none;
            margin: -1px;
        }}

        QDockWidget::float-button {{
            border: none;
            margin: 1px;
        }}

        QDockWidget > * {{
            background-color: {background};
            border: none;
            border-bottom-right-radius: 4px;
            border-bottom-left-radius: 4px;
            titlebar-close-icon: url(/:16_dark_tab-close.svg);
        }}

        QDockWidget::title {{
            background-color: {background};
            border: none;
        }}"""
    flat_toolbar_style = f"""QToolBar {{
            background-color: {background};
            border: none;
        }} """
    flat_menu_bar_style = f"QMenuBar {{background-color: {background};}}"
    flat_combo_box_style = f"""QComboBox {{ 
            background-color: {background};
            border: none;
            border-radius: 4px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            padding-top: 2px;
        }}
        
        QComboBox::drop-down {{
            border: none;
            border-radius: 4px;
        }}
        
        QComboBox::down-arrow {{
            image: url(:16_light_draw-arrow-down.svg);
            width: 9px;
        }}"""
    flat_spin_box_style = f"""QSpinBox {{
            border: none;
            border-radius: 4px;
        }}    

        QSpinBox::up-button {{
            border: none;
            border-radius: 4px;
            margin-left: 2px;
            subcontrol-origin: margin;
        }}

         QSpinBox::down-button {{
            border: none;
            border-radius: 4px;
            margin-left: 2px;
            subcontrol-origin: padding;
        }}

        QSpinBox::up-arrow {{
            image: url(:16_light_draw-arrow-up.svg);
            width: 9px;
        }}

         QSpinBox::down-arrow {{
            image: url(:16_light_draw-arrow-down.svg);
            width: 9px;
        }}"""
    flat_toolbox_style = f"QToolBox {{background-color: {background};}}"   
    flat_status_bar_style = f"QStatusBar {{ background-color: {background}; }}"
    flat_tree_view_style = f"""QTreeView {{
        background-color: {background}; 
        border: none;
    }}"""

def setBackground(new_background):
    global background
    background = new_background

def setAlternate(new_alternate):
    global alternate
    alternate = new_alternate

def setTextColor(new_color):
    global tab_text_color
    tab_text_color = new_color
