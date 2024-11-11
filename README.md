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
        """Add an item with its priority, then sort the queue using Quick Sort with partitioning."""
        self.queue.append((item, priority))
        self.quick_sort(0, len(self.queue) - 1)

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

    def quick_sort(self, low, high):
        """Quick Sort with partition to sort items by priority in descending order."""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        """Partition the list around a pivot for quicksort."""
        pivot = self.queue[high][1]  # using the last element as the pivot
        i = low - 1
        for j in range(low, high):
            if self.queue[j][1] > pivot:  # for descending order
                i += 1
                self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
        self.queue[i + 1], self.queue[high] = self.queue[high], self.queue[i + 1]
        return i + 1

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
