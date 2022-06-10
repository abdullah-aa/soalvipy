import random
import sys
from tokenize import Number
from turtle import right

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
    def topDownSplitMerge(arrA):
        arrB = []
        for element in arrA: arrB.append(element)

        splitMerge(arrB, 0, len(arrA), arrA)

    def splitMerge(arrB, begin, end, arrA):
        if ((end - begin) <= 1): return

        middle = int((end + begin)/2)
        splitMerge(arrA, begin, middle, arrB)
        splitMerge(arrA, middle, end, arrB)

        merge(arrB, begin, middle, end, arrA)

    def merge(arrA, begin, middle, end, arrB):
        left_counter = begin
        right_counter = middle

        for counter in range(begin, end):
            if ((left_counter < middle) and ((right_counter >= end) or (arrA[left_counter] <= arrA[right_counter]))):
                arrB[counter] = arrA[left_counter]
                left_counter += 1
            else:
                arrB[counter] = arrA[right_counter]
                right_counter += 1

    topDownSplitMerge(numbers)

print(numbers)