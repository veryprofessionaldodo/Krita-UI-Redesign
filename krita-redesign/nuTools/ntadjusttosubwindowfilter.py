from krita import Krita 
from PyQt5.QtCore import QObject, QEvent, QPoint

class ntAdjustToSubwindowFilter(QObject):
    """Event Filter object. Ensure that a target widget is moved
    to a desired position (corner of the view) when the subwindow area updates."""
    
    def __init__(self, parent=None):
        super(ntAdjustToSubwindowFilter, self).__init__(parent)
        self.target = None
        

    def eventFilter(self, obj, e):
        """Event filter: Update the Target's position to match to the current view 
        if the (sub-)window has moved, changed in size or been activated."""
        if (self.target and
            (e.type() == QEvent.Move or
            e.type() == QEvent.Resize or
            e.type() == QEvent.WindowActivate)):
            self.target.adjustToView()
            
        return False


    def setTargetWidget(self, wdgt):
        """Set which QWidget to adjust the position of."""
        self.target = wdgt