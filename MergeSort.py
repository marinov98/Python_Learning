def isEmpty(arr):
    if (len(arr) == 0):
        return true
    else:
    return false


def mergSort(array):
    leftIndex = 0
    righIndex = 0

    leftArray = array[:1/2]
    rightArray = arrat[1/2:]

    for i in leftArray:
        for j in rightArray:
