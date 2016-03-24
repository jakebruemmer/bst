class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def compare_left(self, other):
        if self.left_child:
            return self.left_child.value < other.value
        else:
            return True

    def compare_right(self, other):
        if self.right_child:
            return self.right_child.value > other.value
        else:
            return True

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        return self.insert_helper(None, self.root, node)

    def insert_helper(self, parent, curr, node):
        if curr:
            if node.value <= curr.value:
                return self.insert_helper(curr, curr.left_child, node)
            else:
                return self.insert_helper(curr, curr.right_child, node)
        else:
            if node.value <= parent.value:
                parent.left_child = node
                return True
            else:
                parent.right_child = node
                return True
    
    def delete(self, value):
        return self.delete_helper(None, self.root, value)

    def delete_helper(self, parent, curr, value):
        if not curr:
            return False
        elif curr.value == value:
            if not curr.right_child:
                if curr.value <= parent.value:
                    parent.left_child = curr.left_child
                elif curr.value > parent.value:
                    parent.right_child = curr.left_child
            elif curr.right_child <= parent.value:
                parent.left_child = curr.right_child
                parent.left_child = curr.left_child
                return True
            elif curr.right_child > parent.value:
                parent.right_child = curr.right_child
                parent.right_child = curr.left_child
                return True
        elif value <= curr.value:
            return self.delete_helper(curr, curr.left_child, value)
        else:
            return self.delete_helper(curr, curr.right_child, value)

    def search(self, value):
        return self.search_helper(self.root, value)

    def search_helper(self, curr, value):
        if not curr:
            return False
        elif curr.value == value:
            return curr
        elif value < curr.value:
            return self.search_helper(curr.left_child, value)
        else:
            return self.search_helper(curr.right_child, value)

    def __str__(self):
        nodes = [self.root.left_child, self.root.right_child]
        s = [self.root.value].__str__() + "\n"
        while not all(node is None for node in nodes):
            n = []
            for node in nodes:
                if node:
                    s += " [" + str(node.value) + "] " 
                    n.append(node.left_child)
                    n.append(node.right_child)
                else:
                    s += " [] "
                    n + [None, None]
            s += '\n'
            nodes = n
        return s
    
