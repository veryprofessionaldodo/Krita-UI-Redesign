# This file is only useful for debugging. It's never used, and is merely 
# a reminder as to styling can be done (so that I don't forget again)
from krita import * 

instance = Krita.instance()

highlight = qApp.palette().color(QPalette.Highlight).name().split("#")[1]
background = qApp.palette().color(QPalette.Window).name().split("#")[1]
alternate = qApp.palette().color(QPalette.AlternateBase).name().split("#")[1]
inactive_text_color = qApp.palette().color(QPalette.ToolTipText).name().split("#")[1]
active_text_color = qApp.palette().color(QPalette.WindowText).name().split("#")[1]

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


flat_main_window_style = f"""
        QStackedWidget, QStackedLayout {{
            background: #{background};
        }}
        QHeaderView {{
            background: transparent;
            background-color: #{background};
        }}
        
        QLineEdit {{
            background: #{background};
            selection-background-color: #{active_text_color};
        }}

        QStatusBar > * {{
            border: none;
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

        QToolButton::menu-button{{
            background: #{background};
        }}

        QToolButton:hover {{
            background: #{alternate};
        }}

        QToolButton::menu-button:hover {{
            background: #{alternate};
        }}

        QToolButton[popupMode="1"] {{
            padding-right: 13px;
            border: none;
        }}

        QPushButton {{
            background: #{background};
            border: 1px solid #{alternate};
            padding: 5px;
            border-radius: 2px;
        }}

        QPushButton:hover {{
            background: #{alternate};
        }}

        QStatusBar QPushButton {{
            background: #{background};
        }}

        QDoubleSpinBox {{
            border: 1px solid #{alternate};
            border-radius: 2px;
            background: #{background};
        }}

        QDoubleSpinBox::up-button,
        QDoubleSpinBox::up-arrow,        
        QDoubleSpinBox::down-button,
        QDoubleSpinBox::down-arrow {{
            width: 10px;
            height: 10px;
            margin: 3px;
        }}

        QDoubleSpinBox::up-button,
        QDoubleSpinBox::up-arrow {{
            image: url(:24_light_draw-arrow-up.svg);
            margin-top: 1px;
         }}
        
        QDoubleSpinBox::down-button,
        QDoubleSpinBox::down-arrow {{
            image: url(:24_light_draw-arrow-down.svg);
            margin-bottom: 1px;
        }}
    """

flat_welcome_page = f"""
    QPushButton {{
        border: none;
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

def recursive_remove_border(element):
    if hasattr(element, 'setFrameStyle'):
        element.setFrameStyle(QFrame.NoFrame)
    if hasattr(element, 'setFrameShape'):
        element.setFrameShape(QFrame.NoFrame)
    if hasattr(element, 'setFrameShadow'):
        element.setFrameShadow(QFrame.Plain)
    if hasattr(element, 'setLineWidth'):
        element.setLineWidth(0)

    for child in element.children():
        recursive_remove_border(child)

# get random element
elem = window.findChild(QWidget, 'listLayers')
elem2 = elem.findChild(QWidget, 'qt_scrollarea_viewport')

recursive_remove_border(elem)
recursive_remove_border(elem2)

welcomePage = window.findChild(QWidget, 'KisWelcomePage')
welcomePage.setStyleSheet(flat_welcome_page)