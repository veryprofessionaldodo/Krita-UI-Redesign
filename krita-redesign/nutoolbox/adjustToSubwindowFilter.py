from krita import Krita 

class AdjustToSubwindowFilter(QObject):
    """Event Filter object. Ensure that a target widget is moved
    to a desired position (corner of the view) when the subwindow area updates."""
    
    def __init__(self, parent=None):
        super(AdjustToSubwindowFilter, self).__init__(parent)
        qWin = Krita.instance().activeWindow().qwindow()
        self.mdiArea = qWin.centralWidget().findChild(QMdiArea)
        self.target = None
        

    def eventFilter(self, obj, e):
        """Event filter: Update the Target's position to match to the current view 
        if the (sub-)window has moved, changed in size or been activated."""
        if (e.type() == QEvent.Move or
            e.type() == QEvent.Resize or
            e.type() == QEvent.WindowActivate):
            self.adjustTarget()
            
        return False
        

    def adjustTarget(self):
        """Adjust the position and size of the Target to that of the active View."""
        view = self.activeView()
        if view and self.target:
            # NOTE: Determining the correct corner position might be better done based 
            # on whether Krita is set to handle multiple documents as 'AdjustToSubwindows'  or 'Tabs'
            
            # pos = self.mdiArea.pos() # Move to top of QMdiArea. Only suitable for 'AdjustToSubwindows' mode.
            pos = self.mdiArea.mapFromGlobal(view.mapToGlobal(QPoint(0,0))) # Move to top left corner of current view. Hacky, but works!
            self.target.move(pos)

            resizeTarget(self)


    def resizeTarget(self):
        """Shrink the Target to fit within the subwindow when 
        the subwindow is too small. """
        view = self.activeView()

        if view and self.target:
            if view.height() < self.target.sizeHint().height():
                self.target.resize(self.target.sizeHint().width(), view.height())
            else:
                self.target.resize(self.target.sizeHint())


    def activeView(self):
        """Get the View widget of the active subwindow."""
        subWin = self.mdiArea.activeSubWindow()
        
        if subWin:
            for child in subWin.children(): 
                if 'view' in child.objectName(): # Grab the View from the active tab/sub-window
                    return child


    def setTargetWidget(self, wdgt):
        """Set which QWidget to adjust the position of."""
        self.target = wdgt