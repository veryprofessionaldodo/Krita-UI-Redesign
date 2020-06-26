from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea

class ScrollAreaContainer(QWidget):

    def __init__(self, scrollArea = None, parent=None):
        super(ScrollAreaContainer, self).__init__(parent)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.scrollArea = None
        
        self.setScrollArea(scrollArea)


    def sizeHint(self):
        """
        Reimplemented function. If a QScrollArea as been set
        the size hint of it's widget will be returned."""
        if self.scrollArea and self.scrollArea.widget():
            return self.scrollArea.widget().sizeHint()

        return super().sizeHint()


    def setScrollArea(self, scrollArea):
        """
        Set the QScrollArea for the conatiner to hold.

        True will be returned upon success and if no prior QScrollArea was set. 
        If another QScrollArea was already set it will be returned so that 
        it can be disposed of properly.
        
        If an invalid arguement (i.e. not a QScrollArea) or the same QScrollArea
        as the currently set one is passed, nothing happens and False is returned."""
        if (isinstance(scrollArea, QScrollArea) and
            scrollArea is not self.scrollArea):
            ret = True

            if not self.scrollArea:
                self.layout().addWidget(scrollArea)
            else:
                self.layout().replaceWidget(self.scrollArea, scrollArea)
                ret = self.scrollArea # set the old QScrollArea to be returned
            
            self.scrollArea = scrollArea
            return ret
        
        return False

    def scrollArea(self):
        return self.scrollArea