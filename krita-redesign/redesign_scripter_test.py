# This file is only useful for debugging. It's never used, and is merely 
# a reminder as to styling can be done (so that I don't forget again)
from krita import * 

instance = Krita.instance()

highlight = qApp.palette().color(QPalette.Highlight).name().split("#")[1]
background = qApp.palette().color(QPalette.Window).name().split("#")[1]
alternate = qApp.palette().color(QPalette.AlternateBase).name().split("#")[1]
inactive_text_color = qApp.palette().color(QPalette.ToolTipText).name().split("#")[1]
active_text_color = qApp.palette().color(QPalette.WindowText).name().split("#")[1]

darker_background = "404040"
lighter_background = "555555"

stretch_tab_base_style = f"""
QTabBar {{
            background-color: #{alternate};
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
      }}
    
"""

flat_tab_base_style = f"""
  QTabBar::tab:!selected {{
            background: #{alternate};
            color: #{inactive_text_color};
        }} 
        
        QTabBar {{
            background-color: #{alternate};
        }}
        
        QMainWindow > QTabBar::tab {{
            margin-top: 5px;
            padding: 5px;
            background: #{background};
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
            border-top-right-radius: 5px;
            border-top-left-radius: 5px;
        }}
        
        QMainWindow > QTabBar {{
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
        }}

        QTabBar::tab:selected {{
            background: #{background};
        }}

       QTabBar::tab:hover {{
           color: #{active_text_color};
       }}
    """

flat_combo_box_style = f"""
        QComboBox {{ 
            background: #{darker_background};
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


flat_main_window_style = f"""
        QStackedWidget, QStackedLayout {{
            background: #{background};
        }}
        QHeaderView {{
            background: transparent;
            background-color: #{background};
        }}
        
        QLineEdit {{
            background: #{alternate};
        }}

        QStatusBar > * {{
            border: none;
        }}

        QDoubleSpinBox::up-button {{
            border: transparent;
        }} 
        
        QToolButton::menu-button{{
            background: #{background};
        }}
        
        QToolButton:hover {{
            background: #{alternate};
        }}
        
        QToolButton::menu-button:hover {{
            background: #{alternate};
        }}
        
        QStatusBar > QPushButton:hover {{
            background: #2e2e2e;
        }}
        """

flat_menu_bar_style = f"""
    QMenuBar {{
        border-bottom: 0px solid white;        
    }} 
"""

flat_layers_docker = f"""
    QHeaderView QWidget {{
        background: red;
    }}
"""

flat_tree_view_style = f"""QTreeView {{
    background-color: #{background}; 
    border: none;
    padding: 5px;
}}"""

flat_button_style = f"""
        QToolButton, QFrame{{
            background: #{background};
            border: none;
        }}

        QToolButton:checked {{
            background: #{alternate};
            border: none;
        }}

        QToolButton:hover {{
            background: #{alternate};
            border: none;
        }}

        QToolButton[popupMode="1"] {{
            padding-right: 13px;
            border: none;
        }}

        QPushButton {{
            background: #{background};
        }}
        
        QPushButton:hover {{
            background: #{alternate};
        }}

        QStatusBar QPushButton {{
            background: #{background};
        }}
        
        """

full_style_sheet = ""
full_style_sheet += f"\n {stretch_tab_base_style} \n"
full_style_sheet += f"\n {flat_tab_base_style} \n"
full_style_sheet += f"\n {flat_button_style} \n"
full_style_sheet += f"\n {flat_combo_box_style} \n"
full_style_sheet += f"\n {flat_layers_docker} \n"
full_style_sheet += f"\n {flat_main_window_style} \n"
full_style_sheet += f"\n {flat_tree_view_style} \n"
full_style_sheet += f"\n {flat_menu_bar_style} \n"
full_style_sheet += f"\n {flat_layers_docker} \n"

# get object to apply styling

window = instance.activeWindow().qwindow()

# apply styling 

window.setStyleSheet(full_style_sheet)

# print color pallette
# regular types are Window, Background, Foreground, WindowText for example
# print(qApp.palette().color(QPalette.Background).name())

# reset stylesheet 
# stylesheet = "QMainWindowLayout {}"
# window.setStyleSheet(stylesheet)

# list children
#for child in window.children():
#    print(child.objectName())

# get random element
elem = window.findChild(QWidget, 'listLayers')
elem2 = elem.findChild(QWidget, 'qt_scrollarea_viewport')

elem.setStyleSheet("background: blue; border: 2px solid white;")
elem2.setStyleSheet("* {background: red; border: 2px solid white;} * > * > * > * {background: green; border: 2px solid black;}")
elem2.setFrameStyle(QFrame.NoFrame)
elem2.setFrameShape(QFrame.NoFrame)
elem2.setLineWidth(0)
elem2.setFrameShadow(QFrame.Shadow)

elem2.setStyleSheet("*::separator {width: 0px; height: 0px;} * > *::separator {width: 0px; height: 0px;}")

elem.setFrameStyle(QFrame.NoFrame)
elem.setFrameShape(QFrame.NoFrame)
elem.setLineWidth(0)
elem.setFrameShadow(QFrame.Shadow) 