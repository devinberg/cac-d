'''
Created on Jul 30, 2013

@author: student
'''

class cncBase(object):
    '''
    This is the parent class that will be inherited by most classes in the CNC project
    '''
    
    
    drawingObjects = []
    image = ""
    selectedTool = 0
    currentMode = 0
    
    
    tool_Point = 0
    tool_Line = 1
    tool_Rect = 2
    tool_Circle = 3
    tool_Arc = 4
    
    mode_doNothing = 0
    mode_Edit = 1
    mode_Draw = 2

    def __init__(self):
        self._name_ = "cncBase"
       
    
    def getDrawingObjects(self):
        return self.drawingObjects
    
    def getImage(self):
        return self.image
    
    def getSelectedTool(self):
        return self.selectedTool
    
    def getCurrentMode(self):
        return self.currentMode
    
    def changeSelectedTool(self, selectedTool):
        if selectedTool == self.tool_Point: self.selectedTool = self.tool_Point
        elif selectedTool == self.tool_Line: self.selectedTool = self.tool_Line
        elif selectedTool == self.tool_Rect: self.selectedTool = self.tool_Rect
        elif selectedTool == self.tool_Circle: self.selectedTool = self.tool_Circle
        elif selectedTool == self.tool_Arc: self.selectedTool = self.tool_Arc
        
    def changeCurrentMode(self, mode):
        if mode == self.mode_doNothing: self.currentMode = self.mode_doNothing
        elif mode == self.mode_Edit: self.currentMode = self.mode_Edit
        elif mode == self.mode_Draw: self.currentMode = self.mode_Draw
        
        