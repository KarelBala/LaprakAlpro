class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data >= self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

    def operator(self):
        return self.data
    
    def left(self):
        return self.left
    
    def right(self):
        return self.right
    
    def parent(self):
        return self.parent
    
    def is_leaf(self):
        return self.right == None and self.left == None
    
    def is_parent(self):
        return self.parent == None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data, None)
            self.size += 1
        else:
            if self.root.insert(data):
                self.size += 1

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def get_root(self):
        return self.root

    def plus_minus(self):
        pass
         
if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.plus_minus())

Yang harus kalian lakukan sekarang adalah membuat sebuah buah fungsi: yang pertama, fungsi minus_plus. Fungsi ini berfungsi untuk menjumlahkan / mengurangkan semua node yang ada di dalam tree. Jika data ganjil, maka kurangkan, dan jika data genap, maka tambahkan. Misal, jika satu tree mempunyai node - node berikut: 20 2 10 2 5, maka hasil akhirnya adalah 29 (20 + 2 + 10 + 2 - 5). Contoh lainnya, jika suatu tree mempunyai node - node berikut: 23 25 27 26, maka hasil akhirnya adalah -49 (- 23 - 25 - 27 + 26).
