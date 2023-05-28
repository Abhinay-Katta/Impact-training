from DLinkedList import Node as N

# TODO:
# 0.x Insertion
# 1. Deletion
# 2.x Search
# 3.x Height
# 4. Diameter


class Node(N):
    def __init__(self, data: int) -> None:

        super().__init__(data)


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int, root: Node) -> Node:
        '''
        Insert an element into the Binary search tree.
        Root node of the Binary search tree can be created in 2 ways:

        - BST_class_obj.root_name = Node(value)
        - BST_class_obj.root_name = bstree.insert(value, root=None)

        Other leaf nodes should be inserted as:
        - bstree.insert(value, root=BST_class_obj.root_name)

        '''
        if root is None:
            return Node(value)
        if value > root.data:
            root.next = self.insert(value=value, root=root.next)
        elif value < root.data:
            root.prev = self.insert(value=value, root=root.prev)
        return root

    def deletion(self, root: Node, value: int) -> None:
        '''Research going on. To be implemented. Deletes the given value from the Binary Search Tree.'''
        # case1:
        current = self.root
        while root:
            if value > root.data:
                current = root
                root = root.next
            elif value < root.data:
                current = root
                root = root.prev
            elif value == root.data and not root.next and not root.prev:
                root = None
                # root.data = None
                break
            elif value == root.data and not root.next and root.prev:
                current.prev = root.prev
                break
            elif value == root.data and not root.prev and root.next:
                current.next = root.next
                break
            return
        # 3 cases:
        # 1. no child nodes / value to be deleted is a leaf node
        # 2. one child node left or right
        # 3. 2 child nodes: replace with inorder successor
        # 4. left max has a child

    def traverse(self, root: Node) -> None:
        '''Traverses and prints the Binary Search Tree.'''
        if root is not None:
            self.traverse(root=root.prev)
            print(root.data, end=', ')
            self.traverse(root=root.next)

    def inorder_predecessor(self, root: Node) -> Node:
        if root.prev is not None:
            root = self.inorder_predecessor(root=root.prev)
        return root

    def search(self, value: int, root: Node, return_node=False) -> int:
        '''Traverses the Binary Search tree and returns True if the value is found else returns None.
            - If return_value is given as True, the value, if found the value will be returned.
            - return_value = False by default.
        '''
        count = 0
        while root is not None:
            count += 1
            if value < root.data:
                # return self.search(root=root.prev, value=value,) with these, the default parameter cannot be passed
                root = root.prev
            elif value > root.data:
                # return self.search(root=root.next, value=value) with these, the default parameter cannot be passed
                root = root.next
            elif value == root.data:
                if return_node:
                    return root
                else:
                    return True
            return False

    def height(self, root: Node) -> int:
        '''Calculates and returns the height of the Binary Search Tree from the root.
            - Height is basically the length of the longest path from the root node to leaf node.
        '''
        if root is None:
            return 0
        elif root:
            H = 1+max(self.height(root=root.prev), self.height(root=root.next))
            return H

    def diameter(self, root: Node) -> int:
        '''
        - To Be implmented.
        - Calculates and returns the height of the Binary Search Tree from the root. 
        - Diameter is something I still don't know, still researching.
        '''
        pass


asd = BST()
asd.root = Node(10)
asd.insert(value=12, root=asd.root)
asd.insert(value=13, root=asd.root)
asd.insert(value=9, root=asd.root)
asd.insert(value=8, root=asd.root)
asd.insert(value=14, root=asd.root)
asd.traverse(root=asd.root)
print()
# print(asd.inorder_predecessor(root=asd.root).data)
asd.deletion(root=asd.root, value=14)
asd.traverse(root=asd.root)
