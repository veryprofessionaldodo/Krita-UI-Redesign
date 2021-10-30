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

stylesheet = """
QAbstractScrollArea {
   background: red;
   border: none;
}
"""

# get object to apply styling

window = instance.activeWindow().qwindow()

print(window)

# apply styling 

window.setStyleSheet(stylesheet)
window.setStyleSheet(flat_tab_base_style)

# print color pallette
# regular types are Window, Background, Foreground, WindowText for example
print(qApp.palette().color(QPalette.ToolTipBackground).name())

# reset stylesheet 
# window.setStyleSheet("")