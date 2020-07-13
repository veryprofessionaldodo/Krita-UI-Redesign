from PyQt5.QtWidgets import QToolButton, QSizePolicy
from PyQt5.QtCore import Qt, QSize

class ntToggleVisibleButton(QToolButton):

    COLOR_BACKGROUND = '#70000000'
    COLOR_HOVER = '#1c1c1c'
    COLOR_PRESSED = '#53728e'
    STYLE = f"""
        QToolButton {{
            background-color: {COLOR_BACKGROUND};
            border: none;
            border-radius: 4px;
        }}
        
        QToolButton:hover {{
            background-color: {COLOR_HOVER};
        }}
        
        QToolButton:pressed {{
            background-color: {COLOR_PRESSED};
        }}
        """

    def __init__(self, parent = None):
        super(ntToggleVisibleButton, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.setIconSize(QSize(11, 11))
        self.setStyleSheet(self.STYLE)

    def setArrow(self, alignment):
        if alignment == "right":
            self.setArrowType(Qt.ArrowType.RightArrow)
        else:
            self.setArrowType(Qt.ArrowType.LeftArrow)
        