"""
Heapify has time complexity of O(n)
"""
def heapify_max(arr, n, i):
    largest = i # Initialize largest as root
    left = (2 * i) + 1
    right =(2 * i) + 2

    #Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right <  n and arr[right] > arr[largest]:
        largest = right

    # Change root if need be(largest has changed)
    if largest != i: 
        arr[i], arr[largest] = arr[largest],arr[i] # swap

        #Hepify the root
        heapify_max(arr, n, largest)    

def heapSort(arr):
    n =  len(arr)

    #Build a maxHeap
    for i in range(floor(n/2) - 1,-1 ,-1):
        heapify_max(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0],arr[i] # swap
        heapify_max(arr, i, 0)  

    return arr     

arr = [12,11,13,5,6,7]
x = heapSort(arr)
print(x)
