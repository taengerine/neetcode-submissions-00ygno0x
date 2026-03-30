class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity            # max size 
        self.size = 0                       # size for actual stored elements 
        self.array = [0] * self.capacity    # the acutal arrays

    def get(self, i: int) -> int:           
        return self.array[i]                # return array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n 
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        array2 = [0] * self.capacity

        for i in range(self.size):
            array2[i] = self.array[i]
        self.array = array2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity 
