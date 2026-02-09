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
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette

highlight = QApplication.instance().palette().color(QPalette.ColorRole.Highlight).name().split("#")[1]
background = QApplication.instance().palette().color(QPalette.ColorRole.Window).name().split("#")[1]
alternate = QApplication.instance().palette().color(QPalette.ColorRole.AlternateBase).name().split("#")[1]
inactive_text_color = QApplication.instance().palette().color(QPalette.ColorRole.ToolTipText).name().split("#")[1]
active_text_color = QApplication.instance().palette().color(QPalette.ColorRole.WindowText).name().split("#")[1]

small_tab_size = 20
doc_tab_bar_selector = "QMdiArea QTabBar, QMdiArea > QTabBar"
doc_tab_selector = "QMdiArea QTabBar::tab"
doc_tab_selector_alt = "QMdiArea > QTabBar::tab"

no_borders_style = " QToolBar { border: none; } "
small_tab_style = f"""
{doc_tab_selector},
{doc_tab_selector_alt} {{
    height: {small_tab_size}px;
}}"""

nu_toolbox_style = ""
nu_tool_options_style = ""
nu_toggle_button_style = ""
nu_scroll_area_style = ""

""" FLAT THEME """

flat_tab_base_style = ""
flat_tab_big_style = ""
flat_tab_small_style = ""
flat_main_window_style = ""
flat_tool_button_style = ""
flat_push_button_style = ""
flat_button_style = ""
flat_dock_style = ""
flat_toolbar_style = ""
flat_menu_bar_style = ""
flat_combo_box_style = ""
flat_toolbox_style = ""
flat_status_bar_style = ""
flat_tree_view_style = ""
flat_overview_docker_style = ""


def buildNuToolsTheme():
    global nu_toolbox_style
    global nu_tool_options_style
    global nu_toggle_button_style
    global nu_scroll_area_style

    nu_toolbox_style = """
            QWidget {
                background-color: transparent;
                color: palette(window-text);
            }

            QScrollArea {
                background-color: transparent;
            }

            QScrollArea * {
                background-color: transparent;
            }

            QAbstractButton {
                background-color: palette(button);
                color: palette(window-text);
                border: none;
                border-radius: 4px;
            }

            QAbstractButton:checked {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }

            QAbstractButton:hover {
                background-color: palette(alternate-base);
            }

            QAbstractButton:pressed {
                background-color: palette(dark);
            }

            QAbstractButton:disabled {
                color: palette(mid);
            }
        """
    nu_tool_options_style = """
        QWidget#toolOptionsPad {
            background-color: transparent;
            color: palette(window-text);
        }

        QWidget#toolOptionsPadContainer {
            background-color: palette(window);
            border: none;
            border-radius: 8px;
        }

        QWidget#toolOptionsPadContainer QWidget {
            border: none;
        }

        QWidget#toolOptionsPad QAbstractButton,
        QWidget#toolOptionsPad QComboBox,
        QWidget#toolOptionsPad QSpinBox,
        QWidget#toolOptionsPad QDoubleSpinBox,
        QWidget#toolOptionsPad KisSliderSpinBox {
            background-color: palette(base);
            color: palette(text);
            border: none;
            border-radius: 4px;
        }

        QWidget#toolOptionsPad QCheckBox::indicator {
            width: 14px;
            height: 14px;
            border: 1px solid palette(mid);
            border-radius: 2px;
            background-color: palette(base);
        }

        QWidget#toolOptionsPad QCheckBox::indicator:checked {
            border-color: palette(highlight);
            background-color: palette(highlight);
        }
        """
    nu_toggle_button_style = """
        QToolButton {
            background-color: palette(button);
            color: palette(window-text);
            border: none;
            border-radius: 4px;
        }

        QToolButton:hover {
            background-color: palette(alternate-base);
        }

        QToolButton:pressed {
            background-color: palette(dark);
        }
        """
    nu_scroll_area_style = """
        QScrollArea {
            background-color: palette(window);
            color: palette(window-text);
        }
    """


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
        {doc_tab_bar_selector} {{
            background-color: #{alternate};
            border: none;
            qproperty-drawBase: 0;
            qproperty-expanding: 1;
        }}

        {doc_tab_selector},
        {doc_tab_selector_alt} {{
            background: #{alternate};
            color: #{inactive_text_color};
            border: none;
            margin: 0px;
            padding-left: 18px;
            padding-right: 18px;
            padding-top: 6px;
            padding-bottom: 6px;
        }}

        {doc_tab_selector}:selected,
        {doc_tab_selector_alt}:selected {{
            background: #{background};
            color: #{active_text_color};
        }}

        {doc_tab_selector}:hover,
        {doc_tab_selector_alt}:hover {{
            color: #{active_text_color};
        }}
       """
    flat_tab_big_style = f"""
        {doc_tab_selector},
        {doc_tab_selector_alt} {{
            height: 34px;
        }}"""
    flat_tab_small_style = f"""
        {doc_tab_selector},
        {doc_tab_selector_alt} {{
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
            background: #{alternate};
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
            width: 9px;
        }}"""
    flat_toolbox_style = "* > QToolButton {border: none;}"
    flat_status_bar_style = f"QStatusBar {{ background-color: #{background}; }}"
    flat_tree_view_style = f"""QTreeView {{
        background-color: #{background};
        border: none;
        padding: 5px;
    }}"""


buildNuToolsTheme()
buildFlatTheme()
