class Data:
    def __init__(self, json, button_name_of_origin=None):
        self.json = json
        self.button_name_of_origin = button_name_of_origin

    def __str__(self):
        return f"JSON Data: {self.json}, Origin Button: {self.button_name_of_origin}"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print('  ' * level + str(self.data))
        for child in self.children:
            child.display(level + 1)
