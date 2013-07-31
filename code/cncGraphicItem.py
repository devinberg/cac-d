'''
Created on Jul 30, 2013

@author: student
'''
from cncBase import cncBase


class cncGraphicItem(object):
    baseObj = None
    
    name = None
    itemType = None
    xPos = None
    yPos = None
    
    
    #operationType determines if a new object is being constructed, or if one is being made from a list. 0 is new, 1 is create from list
    def __init__(self, cncBaseObj, xPos, yPos, itemType = cncBase.tool_Point, operationType = 0):
        self.baseObj = cncBaseObj
        self.itemType = itemType
        self.xPos = xPos
        self.yPos = yPos
        if operationType == 0:
            #Implement code here so it can use a name from a list. ie cirlce_1, circle_2, rect_1 etc.
            pass
    
    
    def __repr__(self):
        return self.name+','+self.itemType+','+self.xPos+','+self.yPos
    def __str__(self):
        return self.name+','+self.itemType+','+self.xPos+','+self.yPos
    
    def returnObjFromList(self, cncBaseObj, dataFromList = []):
        tempItem = cncGraphicItem(cncBaseObj, dataFromList[1], dataFromList[2], dataFromList[3], 1)
        tempItem.changeName(dataFromList[0])
        return tempItem
        
      
            
    def getName(self):
        return self.name
    def getItemType(self):
        return self.itemType
    def getXPos(self):
        return self.xPos
    def getYPos(self):
        return self.yPos
    
    def changeName(self, newName):
        self.name = newName
    def changeItemType(self, itemType): #This method shouldn't really be used
        self.itemType = itemType
    def changeXPos(self, pos):
        self.xPos = pos
    def changeYPos(self, pos):
        self.yPos = pos
    
    
        
    
            
        

    
    
    
    
    
        
    
        