import argparse

OptionsParser = argparse.ArgumentParser()
OptionsParser.add_argument('--remove', '-r', default=False, action='store_true', required=False, help="remove")
OptionsParser.add_argument('--category', '-c', default='none', required=False, help="add to category")
OptionsParser.add_argument('--item', '-i', default='none', required=False, help="add to item")
OptionsParser.add_argument('--add', '-a', default=False, action='store_true', required=False, help="add")
OptionsParser.add_argument('--listtd', '-l', default=False, action='store_true', required=False, help="list")
args = OptionsParser.parse_args()

def PrintOptions():
    print "Delete:    " + args.remove
    print "Add:       " + args.add
    print "Category:  " + args.category
    print "List:      " + args.listtd

