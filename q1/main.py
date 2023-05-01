
import random
import time

def insertion_sort(arr):
    
    if len(arr) <= 1:
      return
    
    for i in range(1, len(arr)):
         
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key



def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
 
def quicksort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quicksort(array, low, pi - 1)
 
        quicksort(array, pi + 1, high)



        
n = 50
m = 100


print("n: {}".format(n))

insertion_time = 0

for _ in range(10):
    start = time.time()
    for _ in range(m):
        random_array = [random.randint(1, 1000) for _ in range(n)]
        insertion_sort(random_array)
    end = time.time()
    insertion_time += (end-start) / m * 1000000

insertion_time /= 10

print("Insertion Sort: {}".format(insertion_time))



quicksort_time = 0

for _ in range(10):
    start = time.time()
    for _ in range(m):
        random_array = [random.randint(1, 1000) for _ in range(n)]
        quicksort(random_array, 0, len(random_array) - 1)
    end = time.time()
    quicksort_time += (end-start) / m * 1000000

quicksort_time /= 10

print("Quick Sort: {}".format(quicksort_time))

