from perlist import PerList
import sys
from argparser import args, PrintOptions

#
# support enum in python 2.7
#
def enum(**enums):
    return type('Enum', (), enums)

def main():
    
    # Print parsed arguments
    #PrintOptions()
    
    #print "hello"
    
    plist = PerList("")
    plist.loadList()
   
    if args.listtd == True:
        plist.showList()

    if args.add == True:
        if args.category != "none":
            if args.item != "none":
                print "adding item " + args.item + " to category " + args.category
                plist.addItemToCategory(args.category, args.item)
            else:
                print "adding category " + args.category
                plist.addCategory(args.category)
    
    elif args.remove == True:
        if args.category != "none":
            if args.item != "none":
                print "removing item " + args.item + " from category " + args.category
                plist.removeItemFromCategory(args.category, args.item)
            else:
                print "removing category " + args.category
                plist.removeCategory(args.category)


    plist.addCategory("one")
    plist.addCategory("two")

    #plist.showAllLists()
  
    plist.persistList()
    
    #print "bye"


if __name__ == "__main__":
    main()
