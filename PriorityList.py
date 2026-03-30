class DoublyLinkedList:

    # The __Node class contains the reference to both the following node (forward)
    # and to the previous node (backward).
    class __Node:
        # default value of data, forward and backward is none if no data is passed
        def __init__(self, data=None, forward=None, backward=None):
            self.data = data
            self.forward = forward
            self.backward = backward

        def __str__(self):
            return str(self.getData())

        # method to update the data field of Node
        def updateData(self, data):
            self.data = data

        # method to set Forward field the Node
        def setForward(self, node):
            self.forward = node

        # method to set Backward field the Node
        def setBackward(self, node):
            self.backward = node

        # method returns data field of the Node
        def getData(self):
            return self.data

        # method returns address of the next Node
        def getNextNode(self):
            return self.forward

        # method returns address of the previous Node
        def getPreviousNode(self):
            return self.backward


    def __init__(self, contents=[]):
        self.first = DoublyLinkedList.__Node(None,None,None)
        self.last = self.first
        self.numItems = 0
        for e in contents:
            self.addToEnd(e)

    # method adds elements to the left of the Linked List
    def addToStart(self, data):
        # create a temporary node
        tempNode = DoublyLinkedList.__Node(data)
        tempNode.setForward(self.first.getNextNode())
        tempNode.setBackward(self.first)
        if self.first.getNextNode():
            self.first.getNextNode().setBackward(tempNode)
        self.first.setForward(tempNode)
        if self.last is self.first:
            self.last = tempNode
        self.numItems += 1

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):
        tempNode = DoublyLinkedList.__Node(data)
        self.last.setForward(tempNode)
        tempNode.setBackward(self.last)
        self.last = tempNode
        self.numItems += 1

    # method to return an istance of node of the Linked List
    def createNode(data=None):
        return DoublyLinkedList.__Node(data)

    # method displays Linked List
    def display(self):
        if self.first is self.last:
            print("Empty List!!!")
            return False

        node = self.first.getNextNode()
        while node is not self.last:
            print(node, end=" ")
            print("-->", end=" ")
            node = node.getNextNode()
        # do last iteration
        print(self.last)

    # method displays all the links of Linked List
    def displayLinks(self):
        if self.first is self.last:
            print("Empty List!!!")
            return False

        node = self.first.getNextNode()
        while node is not self.last:
            print(node.getPreviousNode(),"-->",node,"-->",node.getNextNode())
            node = node.getNextNode()
        # do last iteration
        print(self.last.getPreviousNode(),"-->",self.last,"-->",None)

    # method returns length of linked list
    def length(self):
        return self.numItems

    # method returns index of the recieved data
    def index(self, data):
        node = self.first.getNextNode()
        position = 1
        while node is not self.last:
            if node.getData() == data:
                return position
            else:
                position += 1
                node = node.getNextNode()
        # do last iteration
        if self.last.getData() == data:
            return self.numItems

    # method returns the data at given position
    def atIndex(self, position):
        if position == self.numItems:
            return self.last.getData()

        node = self.first.getNextNode()
        position = int(position)
        pos = 1
        while pos != position:
            node = node.getNextNode()
            pos += 1
        data = node.getData()
        return data

    # method removes element passed from the Linked List
    def remove(self, data):
        found = False
        node = self.first.getNextNode()
        while not found and node is not self.last:
            if node.getData() == data:
                found = True
            else:
                node = node.getNextNode()
        # do last iteration
        if not found and self.last.getData() == data:
            found = True

        # if previous is None then the data is found at first position
        if found:
            node.getPreviousNode().setForward(node.getNextNode())
            if node.getNextNode():
                node.getNextNode().setBackward(node.getPreviousNode())
            else: # removed last node
                self.last = node.getPreviousNode()
            self.numItems -= 1
            del node
        return found

    # method inserts element to the Linked List in given position
    def insert(self, data, position):
        if position == 1:
            self.addToStart(data)
        elif position == self.numItems:
            self.addToEnd(data)
        elif position > self.numItems:
            raise RuntimeError()
        else:
            tempNode = DoublyLinkedList.__Node(data)
            node = self.first.getNextNode()
            position = int(position)
            pos = 1
            while pos != position:
                node = node.getNextNode()
                pos += 1
            self.attach(tempNode, node, position='before')
            #tempNode.setForward(node)
            #tempNode.setBackward(node.getPreviousNode())
            #node.getPreviousNode().setForward(tempNode)
            #node.setBackward(tempNode)
            #self.numItems += 1

    # method returns max data from the List
    def Max(self):
        node = self.first.getNextNode()
        largest = node.getData()
        while node is not self.last:
            if largest < node.getData():
                largest = node.getData()
            node = node.getNextNode()
        # do last iteration
        if largest < self.last.getData():
            largest = self.last.getData()
        return largest

    # method returns minimum data of Linked list
    def Min(self):
        node = self.first.getNextNode()
        smallest = node.getData()
        while node is not self.last:
            if smallest > node.getData():
                smallest = node.getData()
            node = node.getNextNode()
        # do last iteration
        if smallest > self.last.getData():
            smallest = self.last.getData()
        return smallest

    # method returns the index of max data from the List
    def idxMax(self):
        position = 1
        mPos = position
        node = self.first.getNextNode()
        largest = node.getData()
        while node is not self.last:
            if largest < node.getData():
                largest = node.getData()
                mPos = position
            node = node.getNextNode()
            position += 1
        # do last iteration
        if largest < self.last.getData():
            return self.numItems
        return mPos

    # method returns the index of minimum data of Linked list
    def idxMin(self):
        position = 1
        mPos = position
        node = self.first.getNextNode()
        smallest = node.getData()
        while node is not self.last:
            if smallest > node.getData():
                smallest = node.getData()
                mPos = position
            node = node.getNextNode()
            position += 1
        # do last iteration
        if smallest > self.last.getData():
            return self.numItems
        return mPos

    # method returns max node from the List
    def nodeMax(self):
        node = self.first.getNextNode()
        maxNode = node
        while node is not self.last:
            if maxNode.getData() < node.getData():
                maxNode = node
            node = node.getNextNode()
        # do last iteration
        if maxNode.getData() < self.last.getData():
            maxNode = self.last
        return maxNode

    # method returns minimum node from the List
    def nodeMin(self):
        node = self.first.getNextNode()
        minNode = node
        while node is not self.last:
            if minNode.getData() > node.getData():
                minNode = node
            node = node.getNextNode()
        # do last iteration
        if minNode.getData() > self.last.getData():
            minNode = self.last
        return minNode

    # method detaches a node from the Linked List
    def detach(self, node):
        node.getPreviousNode().setForward(node.getNextNode())
        if node is self.last:
            self.last = node.getPreviousNode()
        else:
            node.getNextNode().setBackward(node.getPreviousNode())
        self.numItems -= 1
        del node

    # method attaches a node before or after a node in the Linked List
    def attach(self, newNode, node, position="after"):
        if position == "after":
            if node is self.last:
                self.last = newNode
            else:
                node.getNextNode().setBackward(newNode)
            newNode.setForward(node.getNextNode())
            newNode.setBackward(node)
            node.setForward(newNode)
        elif position == "before":
            node.getPreviousNode().setForward(newNode)
            newNode.setBackward(node.getPreviousNode())
            newNode.setForward(node)
            node.setBackward(newNode)
        else:
            raise RuntimeError()
        self.numItems += 1

    # method removes and returns an element from the Linked List
    def pop(self, position=1):
        if position < 1:
            print("[DoublyLinkedList.pop(self, position)] argument position must be greater than 0!")
            return None
        elif position > self.numItems:
            print("[DoublyLinkedList.pop(self, position)] argument position must be lower than the number of elements!")
            return None
        elif position == self.numItems:
            node = self.last
            data = node.getData()
            node.getPreviousNode().setForward(None)
            self.last = node.getPreviousNode()
            self.numItems -= 1
            del node
            return data

        node = self.first.getNextNode()
        pos = 1
        while pos != position:
            node = node.getNextNode()
            pos += 1
        data = node.getData()
        node.getPreviousNode().setForward(node.getNextNode())
        node.getNextNode().setBackward(node.getPreviousNode())
        self.numItems -= 1
        del node
        return data

    # method returns a copy of the current Linked List
    def copy(self):
        return DoublyLinkedList(self.toList())

    # method to clear LinkedList
    def clear(self):
        self.first.setForward(None)
        self.last = self.first
        self.numItems = 0
        return True

    # method returns count of data recieved
    def count(self, data):
        node = self.first.getNextNode()
        cnt = 0
        while node is not self.last:
            if node.getData() == data:
                cnt += 1
            node = node.getNextNode()
        # do last iteration
        if self.last.getData() == data:
            cnt += 1
        return cnt

    # method returns builtin List of python consisting of Elements of LinkedList
    def toList(self):
        node = self.first.getNextNode()
        tempList = []
        while node is not self.last:
            tempList.append(node.getData())
            node = node.getNextNode()
        # do last iteration
        tempList.append(self.last.getData())
        return tempList

    # method returns string of elements of Linked list
    # the Elements are seperated by seperator if passed else all elements are appended
    def toString(self, separator=""):
        node = self.first.getNextNode()
        finalString = ""
        while node is not self.last:
            finalString += str(node) + separator
            node = node.getNextNode()
        # do last iteration
        finalString += str(self.last)
        return finalString

    # method returns builtin Set of python consisting of Elements of LinkedList
    def toSet(self):
        node = self.first.getNextNode()
        tempSet = set()
        while node is not self.last:
            tempElement = node.getData()
            if tempElement not in tempSet:
                tempSet.add(tempElement)
            node = node.getNextNode()
        # do last iteration
        if self.last.getData() not in tempSet:
            tempSet.add(self.last.getData())
        return tempSet

    # method reverses the LinkedList
    def reverse(self):
        node = self.last
        lastNode = node
        while node is not self.first:
            previousNode = node.getPreviousNode()
            node.setBackward(node.getNextNode())
            node.setForward(previousNode)
            node = previousNode
        self.first.getNextNode().setForward(None)
        self.last = self.first.getNextNode()
        self.first.setForward(lastNode)
        lastNode.setBackward(self.first)

    # method that sorts LinkedList
    def sort(self):
        start = self.first.getNextNode()
        beginNode = start
        while beginNode is not self.last:
            tempNode = beginNode.getNextNode()
            tempNode2 = beginNode
            smallest = beginNode.getData()
            while tempNode is not self.last:
                if smallest > tempNode.getData():
                    smallest = tempNode.getData()
                    tempNode2 = tempNode
                tempNode = tempNode.getNextNode()
            # do last iteration
            if smallest > self.last.getData():
                smallest = self.last.getData()
                tempNode2 = self.last

            # swap data of beginNode and tempNode2
            if tempNode2 is not beginNode:
                temp = beginNode.getData()
                beginNode.updateData(tempNode2.getData())
                tempNode2.updateData(temp)

            beginNode = beginNode.getNextNode()

    # method returns new instance of the sorted LinkedList without changing original LinkedList
    def sorted(self):
        tempList = self.copy()
        tempList.sort()
        return tempList

class Queue:
    def __init__(self):
        self.items = DoublyLinkedList()

    # method to extract an element at the end of the Queue
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError()
        lastIdx = self.items.numItems
        return self.items.pop()

    # method to insert an element at the beginning of the Queue
    def enqueue(self,item):
        self.items.addToEnd(item)

    # method to inspect the first element of the Queue
    def front(self):
        if self.isEmpty():
            print("Empty Queue!!!")
            return None
        return self.items.first.getNextNode().getData()

    # method to check if the Queue is empty
    def isEmpty(self):
        return self.items.numItems == 0

    # method to clear all the elements of the Queue
    def clear(self):
        return self.items.clear()

    # method returns the number of elements in the Queue
    def size(self):
        return self.items.numItems

    # method returns the Queue in string format
    def __str__(self):
        if self.isEmpty():
            return ''
        return self.items.toString()

class PriorityQueue (Queue):
    def __init__(self):
        super().__init__()

    # method to extract the element with highest priority
    def dequeue(self):
        nodeMax = self.items.nodeMax()
        data = nodeMax.getData()
        self.items.detach(nodeMax)
        return data

    # method to inspect the element with highest priority
    def front(self):
        return self.items.nodeMax().getData()

class Data:
    def __init__(self,v,p):
        self.value = v
        self.priority = p

    # method returns the Data in string format
    def __str__(self):
        return str(self.value)

    # method returns True if two Data are equal
    def __eq__(self,other):
        return self.priority == other.priority

    # method returns True if Data is greater than other
    def __gt__(self,other):
        return self.priority > other.priority

    # method returns True if Data is greater or equal than other
    def __ge__(self,other):
        return self.priority >= other.priority

    # method returns True if Data is lower than other
    def __lt__(self,other):
        return self.priority < other.priority

    # method returns True if Data is lower or equal than other
    def __le__(self,other):
        return self.priority <= other.priority
