from Queue_Stack import Queue

if __name__ == '__main__':

    def display():
        print(Queue.arr)
        n = int(input("Choose the queue size:\t"))
        obj = Queue(n)
        while True:
            opt = int(input('Select the operation:\n1-) Enqueue\n2-) Dequeue\n3-) Stack\n4-) Quit\t'))
            if opt == 1:
                obj.enqueue()
            elif opt == 2:
                obj.dequeue()
            elif opt == 3:
                obj.stack()
            elif opt == 4:
                break
            else:
                print('Invalid option!!!')

    display()
