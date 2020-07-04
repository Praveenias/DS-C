class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_ata_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_at_Value(self,value,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        if value==0:
            self.insert_ata_beginning(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==value-1:
                node=Node(data,itr.next)
                itr.next=node
            count+=1
            itr=itr.next
    def printll(self):
        if self.head is None:
            print("LINKED LIST IS EMPTY")
            return
        itr=self.head
        while itr.next:
            print(itr.data,"-->")
            itr=itr.next
        print(ll)
    def get_length(self):
        if self.head is None:
            return "LINKED LIST IS EMPTY"
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def delete_at_begenning(self):
        self.head=self.head.next
    def delete_at_index(self,index):
        if index==0:
            self.delete_at_begenning()
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def insert_list(self,list):
        for i in list:
            self.insert_at_end(i)


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_list([30,40,50,60])
    ll.printll()

