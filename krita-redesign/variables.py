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

from krita import *

highlight = qApp.palette().color(QPalette.Highlight).name().split("#")[1]
background = qApp.palette().color(QPalette.Window).name().split("#")[1]
alternate = qApp.palette().color(QPalette.AlternateBase).name().split("#")[1]
inactive_text_color = qApp.palette().color(QPalette.ToolTipText).name().split("#")[1]
active_text_color = qApp.palette().color(QPalette.WindowText).name().split("#")[1]

small_tab_size = 20

no_borders_style = " QToolBar { border: none; } "
nu_toolbox_style = f"""
            QWidget {{ 
                background-color: #01{alternate};
            }}
            
            .QScrollArea {{ 
                background-color: #00{background};
            }}
            
            QScrollArea * {{ 
                background-color: #00000000;
            }}
            
            QScrollArea QToolTip {{
                background-color: #{active_text_color};                         
            }}
            
            QAbstractButton {{
                background-color: #aa{background};
                border: none;
                border-radius: 4px;
            }}
            
            QAbstractButton:checked {{
                background-color: #cc{highlight};
            }}
            
            QAbstractButton:hover {{
                background-color: #{highlight};
            }}
            
            QAbstractButton:pressed {{
                background-color: #{alternate};
            }}
        """
nu_toggle_button_style = f"""
        QToolButton {{
            background-color: #aa{background};
            border: none;
            border-radius: 4px;
        }}
        
        QToolButton:hover {{
            background-color: #{highlight};
        }}
        
        QToolButton:pressed {{
            background-color: #{alternate};
        }}
        """

nu_scroll_area_style = f"""
        QScrollArea {{ 
            background-color: red;
            color: red;
        }}
            
        """
small_tab_style = f"QTabBar::tab {{ height: {small_tab_size}px; }}"

""" FLAT THEME """

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
            background: #{background};
        }} 

        * > QSpinBox {{
            border: none;
            background-color: #{alternate};
            border-radius: 4px;
        }}    
    """

    flat_tab_base_style = f"""
        QTabBar::tab:!selected {{
            background: #{alternate};
            border-bottom: 10px solid #{alternate};
            border-top: 10px solid #{alternate};
            margin-top: 5px;
            color: #{inactive_text_color};
        }} 
        
        QTabBar::tab:selected {{
            background: #{alternate};
            border-bottom: 10px solid #{background};
            border-top: 10px solid #{background};
            margin-top: 5px;
        }} 

        QTabBar {{
            background-color: #{alternate};
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
        }}
    
        QTabBar::tab:!selected {{
            background: #{alternate};
            border-bottom: 7px solid #{alternate};
            border-top: 7px solid #{alternate};
            margin-top: 5px;
        }}

        QTabBar::tab:selected {{
            background: #{background};
            border-bottom: 7px solid #{background};
            border-top: 7px solid #{background};
            margin-top: 5px;
        }}

       QTabBar::tab:hover {{
           color: #{active_text_color};
       }}
       """
    flat_tab_big_style = f"""QTabBar::tab {{
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
        }}"""
    flat_tab_small_style = f""" 
        QTabBar::tab {{
            border-top:0px;
            border-bottom: 0px;
            border-top-right-radius: 4px;
            border-top-left-radius: 4px;
            height: {small_tab_size}px;
        }}"""

    flat_main_window_style = f"""
        QHeaderView {{
            background: #{alternate};
        }}
        
        QLineEdit {{
            background: #{alternate};
        }}

        QStatusBar > * {{
            border: none;
        }}

        KisDoubleSliderSpinBox {{
            background: #{alternate};
            border: none;
        }} 
        
        QStatusBar > QPushButton:hover {{
            background: #2e2e2e;
        }}
        """
    flat_button_style = f"""QAbstractButton {{
            background: #{background};
            border: none;
        }}

        QAbstractButton:checked {{
            background: #{alternate};
            border: none;
        }}

        QAbstractButton:hover {{
            background: #{alternate};
            border: none;
        }}

        QAbstractButton[popupMode="1"] {{
            padding-right: 13px;
            border: none;
        }}

        QPushButton {{
            background: #{background};
            border-radius: 4px;
            border: 2px solid #{alternate};
        }}
        
        """

    flat_dock_style = f""" 
        QAbstractScrollArea {{
            background: #{background};
            border: none;
        }}
    
        QDockWidget {{
            titlebar-close-icon: url(:/light_deletelayer.svg);
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
            background-color: #{background};
            border: none;
            border-bottom-right-radius: 4px;
            border-bottom-left-radius: 4px;
            titlebar-close-icon: url(/:16_dark_tab-close.svg);
        }}

        QDockWidget::title {{
            background-color: #{background};
            border: none;
            padding: 5px;
            margin-top: 2px;
        }}"""
    flat_toolbar_style = f"""QToolBar {{
            background-color: #{background};
            border: none;
        }}
        """
    flat_menu_bar_style = f"""QMenuBar {{
        background-color: #{background};
        }}
        """
    flat_combo_box_style = f"""QComboBox {{ 
            background: #{background};
            border-bottom: 2px solid #{inactive_text_color};
            border-radius: 4px;
            padding-left: 10px;
            padding-right: 10px;
            padding-bottom: 2px;
            padding-top: 2px;
        }}

        QComboBox:hover {{
            background: #{alternate};
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
    flat_status_bar_style = f"QStatusBar {{ background-color: #{background}; }}"
    flat_tree_view_style = f"""QTreeView {{
        background-color: #{background}; 
        border: none;
        padding: 5px;
    }}"""
