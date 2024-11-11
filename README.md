class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def __len__(self):
        """Return the length of the queue."""
        return len(self.queue)

    def add(self, item, priority):
        """Add an item with its priority, then sort the queue using Quick Sort."""
        self.queue.append((item, priority))
        self.queue = self.quick_sort(self.queue)

    def remove(self):
        """Remove the item with the highest priority (first item in the sorted list)."""
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if not self.is_empty():
            print(self.queue[0][0], self.queue[0][1])

    def print_all(self):
        """Print all items in the queue from highest to lowest priority."""
        for item, priority in self.queue:
            print(item, priority)

    def quick_sort(self, arr):
        """Quick Sort to sort items by priority in descending order."""
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x[1] > pivot[1]]
        right = [x for x in arr[1:] if x[1] <= pivot[1]]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

# Test Case
myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)
myQueue.add('Kezia', 4)
myQueue.print_all()
myQueue.peek()

print()

myQueue.add('Glen', 8)
myQueue.add('Christo', 1)
myQueue.print_all()
myQueue.peek()

print("\n========REMOVE========")
myQueue.remove()
myQueue.print_all()

print()
myQueue.remove()
myQueue.print_all()

print()
myQueue.remove()
myQueue.print_all()

print()
myQueue.add('Saya', 7)
myQueue.print_all()
