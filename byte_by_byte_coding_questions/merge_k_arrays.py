"""
Given k sorted arrays, merge them into a single sorted array.
merge({{​ 1 ​ , ​ 4 ​ , ​ 7 ​ },{​ 2 ​ , ​ 5 ​ , ​ 8 ​ },{​ 3 ​ , ​ 6 ​ , ​ 9 ​ }}) = {​ 1 ​ , ​ 2 ​ , ​ 3 ​ , ​ 4 ​ , ​ 5 ​ , ​ 6 ​ , ​ 7 ​ , ​ 8 ​ , ​ 9 ​ }


Algorithm:
Create a min Heap and insert the first element of all k arrays.
Run a loop until the size of MinHeap is greater than zero.
Remove the top element of the MinHeap and print the element.
Now insert the next element from the same array in which the removed element belonged.
If the array doesn’t have any more elements, then replace root with infinite.
After replacing the root, heapify the tree.
"""
import sys
from typing import List, Optional
Matrix = List[List[int]]

class MinHeapNode:
    def __init__(self, element, index, next_element_index ):
        self.element =  element
        self.i = index
        self.j = next_element_index

class MinHeap:
    def __init__(self, ar: List[MinHeapNode], size: int):
        self.heap_size = size
        self.heap_arr = ar
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1
    """
    A recursive method to heapify a subtree with the root at give index.
    This method assumes that the subtree are already heapified.
    """
    def min_heapify(self, i):
        l =  left(i)
        r = right(i)
        smallest = i
        if l < self.heap_size and self.heap_arr[l].element  < self.heap_arr[i].element:
            smallest = l
        if r < self.heap_size  and self.heap_arr[r].element < self.heap_arr[smallest].element:
            smallest = r 
        if smallest != i:
            swap(self.heap_arr, i, smallest)
            self.min_heapify(smallest)       

    def get_min(self) -> Optional:
        if self.heap_size <= 0:
            return None
        return self.heap_arr[0]    
   
    # Replace root with new root
    def replace_min(self, root):
        self.heap_arr[0] =  root
        self.min_heapify(0)   

def left(i):
    return 2 *  i + 1

def right(i):
    return 2 *  i + 2  

def swap(arr: List[MinHeapNode], i, j):
    temp =  arr[i]
    arr[i] = arr[j] 
    arr[j] =  temp

def merge_k_sorted_arrays(arr: Matrix, k: int):
    print(arr)
    h_arr = []
    result_size = 0
    for i in range(len(arr)):
        node = MinHeapNode(arr[i][0], i, 1)
        h_arr.append(node)
        result_size += len(arr[i])
  
    print(result_size)
    min_heap =  MinHeap(h_arr, k)
    result =  [0] * result_size
    for i in range(result_size):
        root = min_heap.get_min()
        result[i] =  root.element

        if root.j <  len(arr[root.i]):
            root.element = arr[root.i][root.j]
            root.j += 1
        else:
            root.element = sys.maxsize
        min_heap.replace_min(root)
    
    for x in result:
        print(x, end=' ') 
    print()  


if __name__ == '__main__':
    arr = [
        [2,6,12,34],
        [1,9,20,100],
        [23,34,90,2000]
    ]                 
    print('Merged Array:')
    merge_k_sorted_arrays(arr, len(arr))          

