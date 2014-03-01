import argparse

OptionsParser = argparse.ArgumentParser()
OptionsParser.add_argument('--remove', '-r', default='none', required=False, help="delete entry")
OptionsParser.add_argument('--add', '-a', default='none', required=False, help="add entry")
OptionsParser.add_argument('--category', '-c', default='none', required=False, help="add to category")
OptionsParser.add_argument('--listtd', '-l', default='none', required=False, help="list")
args = OptionsParser.parse_args()

def PrintOptions():
    print "Delete:    " + args.remove
    print "Add:       " + args.add
    print "Category:  " + args.category
    print "List:      " + args.listtd

