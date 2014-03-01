from datetime import timedelta, datetime
import json

#
# support enum in python 2.7
#
def enum(**enums):
    return type('Enum', (), enums)

#PowerState = enum(ON=1, TURNINGON=2, GOINGTOIDLE=3, COMINGFROMIDLE=4, IDLE=5, TURNINGOFF=6, OFF=7)

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
            JSONFile = open(self.persistentListFileName, ")
        JSONFile.write(JSONString)
        JSONFile.close()

