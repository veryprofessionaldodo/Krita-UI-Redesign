# The following script is to be ran using the Scripter plugin for Krita
# It gives Krita a flat look usiing CSS 

from krita import *

win =  Application.activeWindow().qwindow()

background = qApp.palette().color(QPalette.Window).name()
alternate = qApp.palette().color(QPalette.AlternateBase).name()

tab_text_color = "#b4b4b4"

# This "theme" breaks a handful of UI elements because of limitations between
# the various interfaces (CSS, Qt, and Krita's API)
win.setStyleSheet ("""

    /* KISMAINWINDOW */
    
    KisMainWindow {
        background-color: """ + background + """;
    } 
    
    KisMainWindow::separator {
        width: 4px;
        height: 4px;
    }
    
        /* QTOOLBUTTON / QPUSHBUTTON */
     
    QToolButton, QPushButton {
        background-color: """ + background + """;
        border-radius: 4px;
    }
    
    QToolButton:hover, QPushButton:hover {
        border: none;
        background-color: """ + alternate + """;
    }
    
    QToolButton[popupMode="1"] {
        padding-right: 13px;
    }
    
    QToolButton::menu-button {
        border: none;
        border-radius: 4px;
    }
    
        /* QDOCKWIDGET */
    
    QDockWidget {
        titlebar-close-icon: url(:/16_dark_tab-close.svg);
        titlebar-normal-icon: url(:/light_duplicatelayer.svg);
        border-radius-bottom-right: 4px;
        border-radius-bottom-left: 4px;
    }
    
    QDockWidget::close-button {
        border: none;
        margin: -1px;
    }
    
    QDockWidget::float-button {
        border: none;
        margin: 1px;
    }
    
    QDockWidget > * {
        background-color: """ + alternate + """;
        border: none;
        border-radius-bottom-right: 4px;
        border-radius-bottom-left: 4px;
        titlebar-close-icon: url(/:16_dark_tab-close.svg);
    }
    
    QDockWidget::title {
        background-color: """ + alternate + """;
        border: none;
    }
    
        /* QTABBAR */
    
    QTabBar {
        background-color: """ + background + """;
        border: none;
        qproperty-drawBase: 0;
        qproperty-expanding: 1;
    }
    
    QTabBar::tab {
        background-color: """ + alternate + """;
        border-top-right-radius: 4px;
        border-top-left-radius: 4px;
        padding: 8px;
    }
    
    QTabBar::tab:!first {
        margin-left: 2px;
    }
    
    QTabBar::tab:!selected {
        background-color: """ + background + """;
        color: """ + tab_text_color + """;
    }
    
    QTabBar::tab:only-one {
        margin: 0px;
    }
    
    QTabBar::tab:hover {
        color: """ + tab_text_color + """;
    }
    
    QTabBar::tab:selected:hover {
        color: white;
    }
    
    
        /* QTOOLBAR */
    
    QToolBar {
        background-color: """ + background + """;
        border: none;
    }
    
    
        /* QMENUBAR */
    
    QMenuBar {
        background-color: """ + alternate + """;
    }
        
        
        /* QSTATUSBAR*/
    
    QStatusBar {
        background-color: """ + background + """;
    }
    
    
        /* QCOMBOBOX  */
     
    QComboBox {
        background-color: """ + background + """;
        border: none;
        border-radius: 4px;
        padding-left: 5px;
        padding-right: 5px;
        padding-bottom: 2px;
        padding-top: 2px;
    }
    
    QComboBox::drop-down {
        border: none;
        border-radius: 4px;
    }
    
    QComboBox::down-arrow {
        image: url(:16_light_draw-arrow-down.svg);
        width: 9px;
    }
    
    
    /* QSPINBOX */
    
    QSpinBox {
        border: none;
        border-radius: 4px;
    }    
    
    QSpinBox::up-button {
        border: none;
        border-radius: 4px;
        margin-left: 2px;
        subcontrol-origin: margin;
    }
    
     QSpinBox::down-button {
        border: none;
        border-radius: 4px;
        margin-left: 2px;
        subcontrol-origin: padding;
    }
    
    QSpinBox::up-arrow {
        image: url(:16_light_draw-arrow-up.svg);
        width: 9px;
    }
    
     QSpinBox::down-arrow {
        image: url(:16_light_draw-arrow-down.svg);
        width: 9px;
    }

    /* QMENUBAR */

    QMenuBar {
        background-color: """ + background + """;
    }

    /* QTOOLBOX */ 

    QToolBox {
        background-color: """ + background + """;
    }
    
""")