from datetime import timedelta, datetime
import json

#
# PerList class
#
class PerList:

    persistentListFileName = "list.json"
    JSONList = []

    def __init__(self, listName):
        self.listName = "list.json"
        self.JSONList = []

    def loadList(self):
        JSONString = ""
        with open (self.persistentListFileName, "r") as plfn:
            JSONString = plfn.read()
        self.JSONList = json.loads(JSONString)
    
    def persistList(self):
        JSONString = json.dumps(self.JSONList)
        JSONFile = open(self.persistentListFileName, "w")
        JSONFile.write(JSONString)
        JSONFile.close()

    def showList(self):
        for k1, v1 in self.JSONList["list"].iteritems():
            print "\n---------------------"
            print "category: " + k1
            for k2, v2 in v1.iteritems():
                print "    " + v2
        print "\n"

    def addCategory(self, category):
        if not self.JSONList["list"].has_key(category):
            self.JSONList["list"][category] = {}

    def addItemToCategory(self, category, item):
        if not self.JSONList["list"].has_key(category):
            self.JSONList["list"][category] = {}
        self.JSONList["list"][category][item] = item

    def removeCategory(self, category):
        del self.JSONList["list"][category]

    def removeItemFromCategory(self, category, item):
        del self.JSONList["list"][category][item]
        pass

