class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:    
    def __init__(self):
       self.head = ListNode(-1)
       self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if curr == None:
                return -1 
            curr = curr.next

        if curr == None:
            return -1 
        return curr.val

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if self.tail == self.head:
            self.tail = new

    def insertTail(self, val: int) -> None:
        if self.tail == self.head:
            self.head.next = ListNode(val)
            self.tail = self.head.next
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index):
            if curr.next == None:
                return False
            curr = curr.next
        if curr.next == None:
            return False
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
