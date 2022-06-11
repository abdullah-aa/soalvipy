import random
import sys
from tokenize import Number
from turtle import left, right

type = sys.argv[1]
num_of_elements = int(sys.argv[2])

numbers = list(range(num_of_elements))
random.shuffle(numbers)
print(numbers)

def swap(to_index, from_index, array):
    temp = array[to_index]
    array[to_index] = array[from_index]
    array[from_index] = temp

if (type == 'bubble'):
    elements_to_check = num_of_elements
    while elements_to_check >= 1:
        new_elements_to_check = 0
        for index in range(1, elements_to_check):
            if (numbers[index - 1] > numbers[index]):
                swap(index, index - 1, numbers)
                new_elements_to_check = index
        elements_to_check = new_elements_to_check

if (type == 'insertion'):
    for index in range(1, num_of_elements):
        temp = numbers[index]
        inner_counter = index - 1
        while (inner_counter >= 0 and numbers[inner_counter] > temp):
            numbers[inner_counter + 1] = numbers[inner_counter]
            inner_counter -= 1
        numbers[inner_counter + 1] = temp

if (type == 'selection'):
    for index in range(num_of_elements):
        smallest = index
        for inner_counter in range(index + 1, num_of_elements):
            if (numbers[smallest] > numbers[inner_counter]):
                smallest = inner_counter
        if (index is not smallest):
            swap(smallest, index, numbers)

if (type == 'merge'):
    def topDownMergeSort(arrA):
        arrB = []
        for element in arrA: arrB.append(element)

        splitMergeSort(arrB, 0, len(arrA), arrA)

    def splitMergeSort(arrB, begin, end, arrA):
        if ((end - begin) <= 1): return

        middle = int((end + begin)/2)
        splitMergeSort(arrA, begin, middle, arrB)
        splitMergeSort(arrA, middle, end, arrB)

        mergeSort(arrB, begin, middle, end, arrA)

    def mergeSort(arrA, begin, middle, end, arrB):
        left_counter = begin
        right_counter = middle

        for counter in range(begin, end):
            if ((left_counter < middle) and ((right_counter >= end) or (arrA[left_counter] <= arrA[right_counter]))):
                arrB[counter] = arrA[left_counter]
                left_counter += 1
            else:
                arrB[counter] = arrA[right_counter]
                right_counter += 1

    topDownMergeSort(numbers)

if (type == 'quick'):
    def lomutoQuickSort(elements):
        quickSort(elements, 0, len(elements) - 1)

    def quickSort(elements, lo, hi):
        if ((lo >= hi) or (lo < 0)): return

        pivot = partition(elements, lo, hi)

        quickSort(elements, lo, pivot - 1)
        quickSort(elements, pivot + 1, hi)

    def partition(elements, lo, hi):
        pivot = elements[hi]
        new_pivot = lo - 1

        for counter in range(lo, hi):
            if (elements[counter] <= pivot):
                new_pivot += 1
                swap(new_pivot, counter, elements)
        
        new_pivot += 1
        swap(new_pivot, hi, elements)

        return new_pivot

    lomutoQuickSort(numbers)

if (type == 'heap'):
    def heapSort(elements):
        heapify(elements)
        
        for end in reversed(range(1, len(elements))):
            swap(0, end, elements)
            siftDown(elements, 0, end -1)
    
    def heapify(elements):
        count = len(elements)
        start = int((count - 1)/2)

        for start in reversed(range(start + 1)):
            siftDown(elements, start, count - 1)

    def siftDown(elements, start, end):
        root = start
        leftChildIndex = lambda parent : (2 * parent) + 1

        while (leftChildIndex(root) <= end):
            leftChild = leftChildIndex(root)
            toSwap = root
            
            if (elements[toSwap] < elements[leftChild]):
                toSwap = leftChild
            if ((leftChild + 1 <= end) and (elements[toSwap] < elements[leftChild + 1])):
                toSwap = leftChild + 1
            if (toSwap == root): 
                return
            else:
                swap(root, toSwap, elements)
                root = toSwap

    heapSort(numbers)


print(numbers)