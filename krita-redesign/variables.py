"""
    Plugin for Krita UI Redesign, Copyright (C) 2020 Kapyia, Pedro Reis

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


background = "black"
alternate = "black"
tab_text_color = "#b4b4b4"
active_text_color = "#eeeeee"

small_tab_size = 20

no_borders_style = " QToolBar { border: none; } "
nu_toolbox_style = """
            QWidget { 
                background-color: #01808085;
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
nu_tool_options_style = """
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
small_tab_style = f"QTabBar::tab {{ height: {small_tab_size}px; }}"

flat_tab_base_style = ""
flat_tab_big_style = ""
flat_tab_small_style = ""
flat_main_window_style = ""
flat_tool_button_style = ""
flat_push_button_style = ""
flat_dock_style = ""
flat_toolbar_style = ""
flat_menu_bar_style = ""
flat_combo_box_style = ""
flat_toolbox_style = ""
flat_status_bar_style = ""
flat_tree_view_style = ""
flat_overview_docker_style = ""


def buildFlatTheme():
    global flat_tab_base_style
    global flat_tab_big_style
    global flat_tab_small_style
    global flat_main_window_style
    global flat_button_style
    global flat_dock_style
    global flat_toolbar_style
    global flat_menu_bar_style
    global flat_combo_box_style
    global flat_toolbox_style
    global flat_status_bar_style
    global flat_tree_view_style
    global flat_overview_docker_style

    flat_overview_docker_style = f"""
        * {{
            background: {background};
        }} 

        * > QSpinBox {{
            border: none;
            background-color: {alternate};
            border-radius: 4px;
        }}    
    """

    flat_tab_base_style = f"""         
        QTabBar::tab:!selected {{
            background: #232323;
            border-bottom: 10px solid #232323;
            border-top: 10px solid #232323;
            margin-top: 5px;
        }} 
        
        QTabBar::tab:selected {{
            background: #3e3e3e;
            border-bottom: 10px solid #323232;
            border-top: 10px solid #323232;
            margin-top: 5px;
        }} 

        QTabBar {{
            background-color: {alternate};
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
        }}
    
        QTabBar::tab:!selected {{
            background: {alternate};
            border-bottom: 7px solid {alternate};
            border-top: 7px solid {alternate};
            margin-top: 5px;
        }}

        QTabBar::tab:selected {{
            background: {background};
            border-bottom: 7px solid {background};
            border-top: 7px solid {background};
            margin-top: 5px;
        }}

        QTabBar::tab:only-one {{
            margin: 0px;
        }}

       QTabBar::tab:hover {{
           color: white;
       }}
       """
    flat_tab_big_style = f"""QTabBar::tab {{
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
            padding: 10px;
        }}"""
    flat_tab_small_style = f""" 
        QTabBar::tab {{
            margin:0px;
            border-top:0px;
            border-bottom: 0px;
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
            height: {small_tab_size}px;
            padding-left: 10px;
            padding-right: 10px;
        }}"""

    flat_main_window_style = f"""
        QHeaderView {{
            background: {alternate};
        }}
        
        QLineEdit {{
            background: {alternate};
        }}

        QStatusBar > * {{
            border: none;
        }}

        KisDoubleSliderSpinBox {{
            background: {alternate};
            border: none;
        }} 
        
        QStatusBar > QPushButton:hover {{
            background: #2e2e2e;
        }}
        """
    flat_button_style = f"""QAbstractButton {{
            background: {background};
            border: none;
        }}

        QAbstractButton:checked {{
            background: {alternate};
            border: none;
        }}

        QAbstractButton:hover {{
            background: {alternate};
            border: none;
        }}

        QAbstractButton[popupMode="1"] {{
            padding-right: 13px;
            border: none;
        }}

        QPushButton {{
            background: {background};
            border-radius: 4px;
            border: 2px solid {alternate};
        }}
        
        """

    flat_dock_style = f""" 
        QAbstractScrollArea {{
            background: {background};
            border: none;
        }}
    
        QDockWidget {{
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
            padding: 5px;
            margin-top: 2px;
        }}"""
    flat_toolbar_style = f"""QToolBar {{
            background-color: {background};
            border: none;
        }}
        """
    flat_menu_bar_style = f"""QMenuBar {{
        background-color: {background};
        }}
        """
    flat_combo_box_style = f"""QComboBox {{ 
            background: {background};
            border-bottom: 2px solid {alternate};
            border-radius: 4px;
            padding-left: 10px;
            padding-right: 10px;
            padding-bottom: 2px;
            padding-top: 2px;
        }}

        QComboBox:hover {{
            background: {alternate};
        }}
        
        QComboBox::drop-down {{
            border: none;
            border-radius: 4px;
        }}
        
        QComboBox::down-arrow {{
            image: url(:16_light_draw-arrow-down.svg);
            width: 9px;
        }}"""
    flat_toolbox_style = "* > QToolButton {border: none;}"
    flat_status_bar_style = f"QStatusBar {{ background-color: {background}; }}"
    flat_tree_view_style = f"""QTreeView {{
        background-color: {background}; 
        border: none;
        padding: 5px;
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
