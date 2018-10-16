def isEmpty(arr):
    if (len(arr) == 0):
        return True
    else:
        return False


def mergSort(array):
    leftIndex = 0
    righIndex = 0

    leftArray = array[:len(array) // 2]
    rightArray = array[len(array) // 2:]

    for i in leftArray:
        for j in rightArray:
            if ( i >= j):
                array[righIndex] = rightArray[righIndex]
                righIndex+=1
            else:
                array[leftIndex] = leftArray[leftIndex]
                leftIndex+=1

    return array



arr = [1, 4, 5, 6, 7, 8, 9, 22, 11]
mergSort(arr)
