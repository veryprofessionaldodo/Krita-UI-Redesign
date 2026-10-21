"""
    Plugin for Krita UI Redesign, Copyright (C) 2020 Kapyia

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


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea

class ntScrollAreaContainer(QWidget):

    def __init__(self, scrollArea = None, parent=None):
        super(ntScrollAreaContainer, self).__init__(parent)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.sa = None
        
        self.setScrollArea(scrollArea)


    def sizeHint(self):
        """
        Reimplemented function. If a QScrollArea as been set
        the size hint of it's widget will be returned."""
        if self.sa and self.sa.widget():
            return self.sa.widget().sizeHint()

        return super().sizeHint()


    def setScrollArea(self, scrollArea):
        """
        Set the QScrollArea for the container to hold.

        True will be returned upon success and if no prior QScrollArea was set. 
        If another QScrollArea was already set it will be returned so that 
        it can be disposed of properly.
        
        If an invalid arguement (i.e. not a QScrollArea) or the same QScrollArea
        as the currently set one is passed, nothing happens and False is returned."""
        if (isinstance(scrollArea, QScrollArea) and
            scrollArea is not self.sa):
            ret = True

            if not self.sa:
                self.layout().addWidget(scrollArea)
            else:
                self.layout().replaceWidget(self.sa, scrollArea)
                ret = self.sa # set the old QScrollArea to be returned
            
            self.sa = scrollArea
            return ret
        
        return False

    def scrollArea(self):
        return self.sa