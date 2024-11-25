class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def plus_minus(root):
    # Fungsi untuk menjumlahkan atau mengurangkan nilai node
    def dfs(node):
        if node is None:
            return 0
        # Jika node genap, tambahkan; jika ganjil, kurangkan
        if node.data % 2 == 0:
            return node.data + dfs(node.left) + dfs(node.right)
        else:
            return -node.data + dfs(node.left) + dfs(node.right)

    return dfs(root)

def find_deepest_leaf(root):
    # Fungsi untuk mencari kedalaman node paling dalam
    if root is None:
        return -1
    
    queue = [(root, 0)]  # Antrian untuk BFS (node, depth)
    deepest_depth = 0
    
    while queue:
        node, depth = queue.pop(0)
        
        # Cek jika node ini adalah leaf
        if node.left is None and node.right is None:
            deepest_depth = max(deepest_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return deepest_depth
