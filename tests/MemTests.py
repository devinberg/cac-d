

class test(object):
    listOfStuff = []

    def addToList(self, wordObject):
        self.listOfStuff.append(wordObject)

    def deleteFromList(self,word):
        self.listOfStuff.remove(word)

class wordObject(object):
    testObject = None
    name = ""

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    
    def __init__(self, testObject, name):
        self.testObject = testObject
        self.name = name

    def removeFromList(self):
        self.testObject.listOfStuff.remove(self)


testObj = test()
wordObject1 = wordObject(testObj, "wordObject1")
wordObject2 = wordObject(testObj, "wordObject2")
wordObject3 = wordObject(testObj, "wordObject3")
wordObject4 = wordObject(testObj, "wordObject4")

testObj.addToList(wordObject1)
testObj.addToList(wordObject2)
testObj.addToList(wordObject3)
testObj.addToList(wordObject4)

print(testObj.listOfStuff)
testObj.listOfStuff.remove(wordObject1)
print(testObj.listOfStuff)

#This is demonstrating removing an item from a list,
#from WITHIN the item itself. This does not leave an object
#floating in memory either, due to the fact that once
#all references to that object are gone it is garbage collected.
wordObject3.removeFromList()
print(testObj.listOfStuff)

'''
testObj.addToList("word1")
testObj.addToList("word2")
testObj.addToList("word3")
testObj.addToList("word4")

print(testObj.listOfStuff)

wordObject1.testObject.listOfStuff.pop()
print(wordObject1.testObject.listOfStuff)

print(wordObject3.testObject.listOfStuff)
print(testObj.listOfStuff)
'''

