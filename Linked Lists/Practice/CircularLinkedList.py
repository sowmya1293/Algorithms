class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def create(self,value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        self.length += 1

    def append(self,value):
        node = Node(value)
        
        self.tail.next = node
        node.next = self.head
        self.tail = node
        self.length +=1

    def deleteNode(self,value): #coding Exercise 36
        prev_node = Node(-1)
        prev_node.next = self.head
        current_node = self.head

        while current_node is not None:
            if(current_node.value == value):
                prev_node.next = current_node.next
                current_node.next = None
                self.length -= 1
                break
            prev_node = current_node
            current_node = current_node.next
            if(current_node == self.head):
                break
        
    def countNodes(self): #coding exercise 37
        current_node = self.head
        count = 0

        while current_node is not None:
            count += 1
            current_node = current_node.next
            if(current_node == self.head):
                break
        print("The number of nodes is/are",count)

    def splitLinkedList(self):  # coding exercise 38 split the linked list into two halves
        first_list = CircularLinkedList()
        second_list = CircularLinkedList()

        mid = (self.length+1)//2
        count = 1
        last_firstList = None
        current = self.head

        while count<=mid:
            first_list.append(current.value)
            last_firstList = current
            current = current.next
            count += 1

        if last_firstList:
            first_list.tail = last_firstList
            first_list.tail.next = first_list.head

        while current!= self.head:
            second_list.append(current.value)
            current = current.next
        
        if second_list.length > 0:
            second_list.tail = self.tail
            self.tail.next = second_list.head

        return first_list, second_list

    def checkSorted(self):  #coding exercise 39
        current_node = self.head

        while current_node is not None:
            if(current_node == self.tail):
                sorted = True
                break
            if(current_node.value<current_node.next.value):
                current_node = current_node.next
            else:
                print("Linked list is not sorted")
                sorted = False
                break
        if(sorted):
            print("Linked list is sorted")

    def insertIntoSortedList(self,value): #coding exercise 40
        node = Node(value)

        current_node = self.head
        while current_node is not None:
            if(current_node == self.tail):
                break
            if(node.value>=current_node.value and node.value<current_node.next.value):
                    temp_node = current_node.next
                    current_node.next = node
                    node.next = temp_node
                    self.length += 1
                    break
            else:
                current_node = current_node.next

        # see coding exercise 41 on Udemy
                   

    def print(self):
        current_node = self.head

        for _ in range(self.length):
            print(current_node.value)
            current_node = current_node.next


circularLinkedList = CircularLinkedList()
circularLinkedList.create(1)
circularLinkedList.append(2)
circularLinkedList.append(3)
circularLinkedList.append(4)
circularLinkedList.append(5)
circularLinkedList.insertIntoSortedList(4)
#circularLinkedList.checkSorted()
# splitLists = circularLinkedList.splitLinkedList()
# print(splitLists)
# circularLinkedList.deleteNode(5)
circularLinkedList.print()
#circularLinkedList.countNodes()