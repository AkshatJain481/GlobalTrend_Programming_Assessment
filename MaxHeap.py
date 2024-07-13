class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        if len(self.heap) == 0:
            return False
        
        try:
            index = self.heap.index(val)
            self.heap[index] = self.heap[-1]
            del self.heap[-1]

            if index < len(self.heap):
                self._heapify_down(index)
            return True
        except ValueError:
            return False

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] > self.heap[largest]):
            largest = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] > self.heap[largest]):
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Function to interactively use the MaxHeap class with error handling
def max_heap_interactive():
    heap = MaxHeap()
    while True:
        print("\nMenu:")
        print("1. Insert a number")
        print("2. Delete a number")
        print("3. Get maximum number")
        print("4. Display current heap")
        print("5. End session")

        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                num = int(input("Enter number to insert: "))
                heap.insert(num)
                print(f"{num} inserted into the heap.")
            elif choice == 2:
                num = int(input("Enter number to delete: "))
                if heap.delete(num):
                    print(f"{num} deleted from the heap.")
                else:
                    print(f"{num} not found in the heap.")
            elif choice == 3:
                max_num = heap.get_max()
                if max_num is not None:
                    print(f"Maximum number in the heap: {max_num}")
                else:
                    print("Heap is empty.")
            elif choice == 4:
                print("Current heap:", heap.heap)
            elif choice == 5:
                print("Ending session.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer choice (1-5).")

# Example usage:
if __name__ == "__main__":
    max_heap_interactive()
