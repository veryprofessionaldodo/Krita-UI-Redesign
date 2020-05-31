from krita import *


def removeBorder(window):
    window.qwindow().setStyleSheet("""
            QToolBar {
                border: none;
            }
        """)


class Redesign(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        removeBorder(window)


Krita.instance().addExtension(Redesign(Krita.instance()))
