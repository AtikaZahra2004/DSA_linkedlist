# Step 1: Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Step 2: Create Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Step 3: Insert at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Step 4: Display Linked List
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Step 5: Create object
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()