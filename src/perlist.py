from datetime import timedelta, datetime
import json
import os

#
# PerList class
#
class PerList:

    persistentListFileName = "list.json"
    JSONList = []

    def __init__(self, listName):
        path = os.path.dirname(os.path.abspath(__file__))
        self.persistentListFileName = path + "/list.json"
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
        try:
            for k1, v1 in self.JSONList["list"].iteritems():
                print "\n---------------------"
                print "category: " + k1
                for k2, v2 in v1.iteritems():
                    print "    " + v2
            print "\n"
        except:
            print "an error occured while printing your list"

    def addCategory(self, category):
        try:
            if not self.JSONList["list"].has_key(category):
                self.JSONList["list"][category] = {}
        except:
            print "adding category '" + category + "' failed."

    def addItemToCategory(self, category, item):
        try:
            if not self.JSONList["list"].has_key(category):
                self.JSONList["list"][category] = {}
            self.JSONList["list"][category][item] = item
        except:
            print "adding item '" + args.item + "' from category '" + args.category + "' failed."

    def removeCategory(self, category):
        try:
            del self.JSONList["list"][category]
        except:
            print "removing category '" + category + "' failed."

    def removeItemFromCategory(self, category, item):
        try:
            del self.JSONList["list"][category][item]
        except:
            print "removing item '" + args.item + "' from category '" + args.category + "' failed."

