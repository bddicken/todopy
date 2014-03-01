from perlist import PerList
import sys

def main():
    # Parse command line arguments
    from argparser import args, PrintOptions
    
    # Print parsed arguments
    PrintOptions()
    
    print "hello"
    
    plist = PerList("")
    plist.loadList()
    plist.persistList()
    
    print "bye"


if __name__ == "__main__":
    main()
