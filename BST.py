from collections import deque

class Bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data==data:
            return False
        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Bst(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Bst(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def delete(self,data):
        if self.data > data:
            if self.left:
                self.left=self.left.delete(data)
        elif self.data < data:
            if self.right:
                self.right=self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)

        return self

    def level_order_traversal(self):
        if self is None:
            return None
        queue=deque()
        queue.append(self)
        while len(queue)> 0:
            ft =queue.popleft()
            print(ft.data,end=" ")
            if ft.left is not None:
                queue.append(ft.left)
            if ft.right is not None:
                queue.append(ft.right)

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def root_tree(l):
    root=Bst(l[0])
    for i in range(1,len(l)):
        root.add_child(l[i])
    return root


if __name__=='__main__':
    l=[5,3,7,4,2,8,6]
    bst=root_tree(l)
    print(bst.in_order_traversal())
    print(bst.pre_order_traversal())
    print(bst.post_order_traversal())
    bst.level_order_traversal()
    bst.delete(7)
    print(bst.in_order_traversal())
