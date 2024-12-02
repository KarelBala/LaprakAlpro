
    def plus_minus(self):
        def helper(node):
            if node is None:
                return 0
            total = 0
            # Traverse left
            total += helper(node.left)
            # Process current node
            if node.data % 2 == 0:  # Even number
                total += node.data
            else:  # Odd number
                total -= node.data
            # Traverse right
            total += helper(node.right)
            return total

        return helper(self.root)