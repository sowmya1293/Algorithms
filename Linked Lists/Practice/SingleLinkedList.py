import math

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def createSLL(self,value):
        node = Node(value)
        node.next = None
        self.head = node
        self.tail = node
        self.length = 1 

    def printSLL(self):
        current_node = self.head

        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def middleOfSLL(self): #find the middle element of the linked list
        temp_node = self.head
        middleIndex = math.floor(self.length/2)

        for _ in range(middleIndex):
            temp_node = temp_node.next
        return temp_node.value
    
    def removeDuplicates(self):
        seen = set()

        dummy = Node(-1)
        dummy.next = self.head
        prev_node = dummy

        current_node = self.head

        while current_node:
            if current_node.value in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.value)
                prev_node = current_node
                current_node = current_node.next
        
        self.printSLL()
    
    def removeElement(self,val): #remove the value of the linked list that matches with the passed value
        dummy = Node(-1)
        dummy.next = self.head
        prev_node = dummy

        current_node = self.head

        while current_node:
            if(current_node.value==val):
                prev_node.next = current_node.next
                current_node = current_node.next

            else:
                prev_node = current_node
                current_node = current_node.next
            
        
        self.printSLL()  

    def palindrome(self):
        prev_node = None
        current_nodeTwo = self.head

        while current_nodeTwo:
            next_node = current_nodeTwo.next
            current_nodeTwo.next = prev_node
            prev_node = current_nodeTwo
            current_nodeTwo = next_node
        self.headTwo = self.tail
        self.tailTwo = self.head

        current_nodeOne = self.head
        current_nodeTwo = self.headTwo
        while current_nodeOne and current_nodeTwo:
            # print(current_nodeOne.value,current_nodeTwo.value)
            if current_nodeOne.value != current_nodeTwo.value:
                return False
            else:
                current_nodeOne = current_nodeOne.next
                current_nodeTwo = current_nodeTwo.next
        return True

    def returnKthFromLast(self,location):   #return Kth element from last    
        current_node = self.head
        k = self.length-location
        i = 0

        while i<k:
            current_node = current_node.next
            i += 1
        return current_node.value
    
    def partition(self):
        current_node = self.head
        mid = self.length/2
        i=0

        list1 = SingleLinkedList()
        while i<mid:
            list1.append(current_node.value)
            current_node = current_node.next
            i += 1
        list1.printSLL()

        i=0
        list2 = SingleLinkedList()
        while i<mid:
            list2.append(current_node.value)
            current_node = current_node.next
            i += 1
        list2.printSLL()

    def sumOfElements(self):    #sum of elements in a linked list
        current_node = self.head
        sum = 0
        while current_node:
            sum = sum+current_node.value
            current_node = current_node.next
        print(sum)

    def intersect(self):    #intersect two linked lists
        list1 = SingleLinkedList()
        list2 = SingleLinkedList()
        seen = set()

        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)

        list2.append(4)
        list2.append(2)
        list2.append(5)
        list2.append(6)

        current_nodeOne = list1.head
        current_nodeTwo = list2.head

        while current_nodeOne:
            seen.add(current_nodeOne.value)
            current_nodeOne = current_nodeOne.next

        while current_nodeTwo:
            if(current_nodeTwo.value in seen):
                current_nodeTwo = current_nodeTwo.next
                continue
            else:
                list1.append(current_nodeTwo.value)
                current_nodeTwo = current_nodeTwo.next
        list1.printSLL()




singleLinkedList = SingleLinkedList()
#singleLinkedList.createSLL(1)
#singleLinkedList.append(2)
#singleLinkedList.append(2)
#singleLinkedList.append(3)
# singleLinkedList.append(2)
# singleLinkedList.append(4)
# singleLinkedList.append(5)
# singleLinkedList.append(6)
# singleLinkedList.append(6)
# midValue = singleLinkedList.middleOfSLL()
# print("The value at the middle of the linked list is",midValue)
# singleLinkedList.removeDuplicates()
# singleLinkedList.removeElement(2)
#singleLinkedList.partition()
#singleLinkedList.sumOfElements()
singleLinkedList.intersect()
"""value = singleLinkedList.returnKthFromLast(1)
print(value)"""
"""value = singleLinkedList.palindrome()
if value:
     print("It's a palindrome")
 else:
     print("It's not a palindrome")"""


