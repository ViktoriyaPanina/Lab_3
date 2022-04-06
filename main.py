from random import randint

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print arr[i]

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)
 
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
 
print(arr)