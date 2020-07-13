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
        