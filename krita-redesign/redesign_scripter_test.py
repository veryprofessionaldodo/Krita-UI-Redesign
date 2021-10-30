# This file is only useful for debugging. It's never used, and is merely 
# a reminder as to styling can be done (so that I don't forget again)
from krita import * 

instance = Krita.instance()

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

# print color pallette
# regular types are Window, Background, Foreground, WindowText for example
print(qApp.palette().color(QPalette.ToolTipBackground).name())