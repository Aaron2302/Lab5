#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#11/27/18
#implement the heap class and heapsort
class Heap:
    heaparray = []
    def __init__(self):
        self.heaparray = []

    def insert(self , val):#inserts an element into the heap and percolates up until it is in the correct location
        self.heaparray.append(val)
        i = len(self.heaparray)-1
        while i > 0:
            parentIndex = (i-1)//2
            if self.heaparray[i] < self.heaparray[parentIndex]: 
                self.heaparray[i] , self.heaparray[parentIndex] = self.heaparray[parentIndex] , self.heaparray[i]
                i = parentIndex
            else:
                return
                
    def extractMin(self):#removes the root from the heap and moves the last element to the root then percolates down until it is in the correct location
        if len(self.heaparray) == 0:
            return None
        result = self.heaparray[0]
        self.heaparray[0] = self.heaparray[len(self.heaparray)-1]
        self.heaparray.pop()
        i = 0
        while i < len(self.heaparray):
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            if leftChild >= len(self.heaparray):
                return result
            minNode = leftChild
            if rightChild < len(self.heaparray):
                if self.heaparray[minNode] > self.heaparray[rightChild]:
                    minNode = rightChild
            if self.heaparray[i] > self.heaparray[minNode]:
                self.heaparray[i] , self.heaparray[minNode] = self.heaparray[minNode] , self.heaparray[i]
            else:
                return result
            i = minNode 
        return result
    
    def isEmpty(self):#returns if the heap is empty
        return len(self.heaparray) == 0
    
    def heapSort(array): #turns an array into a heap then repeatedly removes the min to create a sorted array
        heap = Heap()
        for i in range(len(array)):
            heap.insert(array[i])
        sortedArray = []
        for i in range(len(array)):
            sortedArray.append(heap.extractMin())
        return sortedArray
    
