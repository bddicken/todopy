import argparse

OptionsParser = argparse.ArgumentParser()
OptionsParser.add_argument('--remove', '-r', default=False, action='store_true', required=False, help="Enables removal mode. In removal mode, you can remove categories with the category flag, or remove an item from a category, with a combination of the category and item flags.")
OptionsParser.add_argument('--add', '-a', default=False, action='store_true', required=False, help="Anables add mode. In add mode, you can add categories with the category flag, or add an item to a category, with a combination of the category and item flags. ")
OptionsParser.add_argument('--item', '-i', default='none', required=False, help="Specifies the item to add (if in add mode) or to remove (if in remove mode).")
OptionsParser.add_argument('--category', '-c', default='none', required=False, help="Specifies the category to add (if in add mode) or to remove (if in remove mode).")
OptionsParser.add_argument('--listtd', '-l', default=False, action='store_true', required=False, help="Print the todo list.")
args = OptionsParser.parse_args()

def PrintOptions():
    print "Delete:    " + str(args.remove)
    print "Add:       " + str(args.add)
    print "Category:  " + str(args.category)
    print "List:      " + str(args.listtd)

