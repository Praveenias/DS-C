class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,data):
        data.parent=self
        self.children.append(data)
    def get_level(self):
        p=self.parent
        count=0
        while p:
            count+=1
            p=p.parent
        return count
    def print(self):
        spaces=" "*self.get_level()*3
        print(spaces,self.data)
        if self.children:
            for child in self.children:
                child.print()

def tree_structure():
    tamilnadu=Tree("TAMIL NADU")
    dharmapuri=Tree("DHARMAPURI")
    dharmapuri.add_child(Tree("BOMMIDI"))
    dharmapuri.add_child(Tree("KADATHUR"))
    salem=Tree("salem")
    salem.add_child(Tree("aatur"))
    salem.add_child(Tree("omalur"))
    tamilnadu.add_child(dharmapuri)
    tamilnadu.add_child(salem)
    return tamilnadu
if __name__=='__main__':
    root=tree_structure()
    root.print()
