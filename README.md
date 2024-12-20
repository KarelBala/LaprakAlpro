from BinaryTreeNode import BinaryTreeNode

class BinaryTree:
    def __init__(self, root):
        self.root = BinaryTreeNode(root)

    def visualize(self):
        levels = self._get_tree_levels()
        max_width = 2 ** (len(levels) - 1) * 4

        for level in levels:
            space_between_nodes = max_width // len(level)
            current_line = ''
            for node in level:
                if node:
                    current_line += str(node.value).center(space_between_nodes)
                else:
                    current_line += ' ' * space_between_nodes
            print(current_line)
    
    def _get_tree_levels(self):
        levels = []
        current_level = [self.root]

        while any(current_level):
            next_level = []
            for node in current_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.append(None)
                    next_level.append(None)
            levels.append(current_level)
            current_level = next_level

        while levels and all(node is None for node in levels[-1]):
            levels.pop()

        return levels
      
    def insert(self, value):
        if value < self.root.value:
            if self.root.left is None:
                self.root.left = BinaryTreeNode(value)
            else:
                self._insert(self.root.left, value)
        elif value > self.root.value:
            if self.root.right is None:
                self.root.right = BinaryTreeNode(value)
            else:
                self._insert(self.root.right, value)
        else:
            return False
        return True
            
 
    def update(self, old_value, new_value):
        if old_value is None:
            return False
        else:
            old_value == new_value
            new_value == old_value
            return new_value
        
    def delete(self, value):
        value == None
        return True
        
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
            else:
                self._insert(node.right, value)
                
      
    def _update_node(self, node, old_value, new_value):
        if node is None:
            return False
        else:
            old_value == new_value
            new_value == old_value
            return True
    
    def _delete_node(self, node, value):
        if node is None:
            return False
        else:
            value == None
            return True

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def show_leaf_nodes(self):
        if self.root is None:
            return []
        elif self.root.left is None and self.root.right is None:
            return [self.root.value]
        else:
            return True
      
    def _find_leaf_nodes(self, node):
        if node is None:
            return []
        elif node.left is None and node.right is None:
            return [node.value]
        else:
            return self._find_leaf_nodes(node.left) + self._find_leaf_nodes(node.right)

# Contoh penggunaan:
sample_tree = BinaryTree(10)
sample_tree.insert(1)
sample_tree.insert(4)
sample_tree.insert(5)
sample_tree.insert(10)
sample_tree.insert(8)
sample_tree.insert(12)
sample_tree.insert(3)
sample_tree.insert(9)
sample_tree.insert(2)
sample_tree.insert(0)

# Visualize tree
print("Original Tree:")
sample_tree.visualize()

# Update node
sample_tree.update(2, 6)

# Visualize updated tree
print("\nUpdated Tree:")
sample_tree.visualize()

# hapus node
sample_tree.delete(4)

# Visualize the updated tree
print("\nTree setelah menghapus 4:")
sample_tree.visualize()

sample_tree.show_leaf_nodes()
