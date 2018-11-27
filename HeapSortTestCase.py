#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#11/27/18
#implement the heap class
import unittest
from Lab5 import Heap
import random

class HeapSortTestCase(unittest.TestCase):

    def testSorted(self): #tests if the array created by heap sort is equal to a sorted array
        array = []
        for i in range(100):
            array.append(int(random.random() * 100))
        sortedArray = Heap.heapSort(array)
        array.sort()
        self.assertEqual(sortedArray, array)
        
if __name__ == '__main__':
    unittest.main()
