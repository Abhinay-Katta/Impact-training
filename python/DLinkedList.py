class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data: int) -> None:
        '''
        Insert an node with data at the end of the Doubly Linked List.
        '''

        node = Node(data=data)
        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next is not None:

                current = current.next
            current.next = node
            node.prev = current

    def insert_at_beginning(self, value: int) -> None:
        '''
        Insert an element at the beginning of the Doubly Linked List.
        '''
        current = self.head
        node = Node(value)
        self.head = node
        node.next = current

    def traverse(self) -> None:
        '''
        Print out all the nodes in the Doubly Linked List.
        '''
        current = self.head
        prev = None
        while current is not None:
            print(current.data)
            current.prev = prev
            current = current.next


dll = DLL()
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(300)
dll.traverse()
dll.insert_at_beginning(400)
dll.traverse()
