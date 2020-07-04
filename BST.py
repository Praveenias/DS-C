class Bst:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add_child(self,data):
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Bst(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Bst(data)
    def printt(self):
        ele=[]
        if self.left:
            ele+=self.left.printt()
        ele.append(self.data)
        if self.right:
            ele+=self.right.printt()
        return ele

    def search(self,data):
        if self.data==data:
            return True
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.right
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.left
        return self.left.find_min()
    def delete(self,data):
        if self.data > data:
            if self.left:
                return self.left.delete(data)
        elif self.data < data:
            if self.right:
                return self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

def built_tree(list):
    root=Bst(list[0])
    for ele in range(1,len(list)):
        root.add_child(list[ele])
    return root

if __name__=='__main__':
    list=[2,5,7,6,8,4]
    bt=built_tree(list)
    print(bt.printt())
    print(bt.search(8))
    bt.delete(7)
    print(bt.printt())