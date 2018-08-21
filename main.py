from elves import Elves
from tree import ChristmasTree

config = {'file_name': 'elves.json'}


elves = Elves(config)
elves.write_report()

tree = ChristmasTree()
tree.print_tree_method_one()
tree.print_tree_method_two()
tree.print_tree_method_three()
