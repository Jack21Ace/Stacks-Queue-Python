class Queue:
    arr: list = []
    head: int = 0
    def __init__(self, size):
        self.size = size

    def enqueue(self):
        if len(self.arr) == self.size:
            print("Queue is Full!!!!")
        else:
            self.e = int(input('Enter the new element\n'))
            self.arr[:0] = [self.e]
            print(self.arr)

    def dequeue(self):
        if not self.arr:
            print('Queue is Empty!!')
        else:
            self.head = self.arr[-1]
            tem = self.arr[:-1]
            self.arr = tem
            print(f'Element removed: {self.head}\n{self.arr}')

    def stack(self):
        temp = self.arr[1:]
        self.arr = temp
        print(self.arr)