# Write some code that generates a tree of any size and prints it in the console

# One level:
# *

# Two levels:
# *
# **

# Three levels:
# *
# **
# ***

# Your code here


class ChristmasTree():

    def print_tree_method_one(self):
        height = int(input('Type in the height of the tree: '))

        for i in range(1, height + 1):
            print('*' * i)

    def print_tree_method_two(self):
        height = int(input('Type in the height of the tree: '))

        for row in range(1, height + 1):
            print(' ' * (height - row) + '* ' * row)

    def print_tree_method_three(self):
        height = int(input('Type in the height of the tree: '))

        completed_row = ''
        for row in range(1, height + 1):
            space = ' ' * (height - row)
            for star in range(1, height + 1):
                stars = '* ' * row
                completed_row = space + stars
            print(completed_row)
