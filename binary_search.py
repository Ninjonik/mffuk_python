def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) // 2

        print(left, right, middle, array[middle])

        if array[middle] == target:
            return middle

        if array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

print(binary_search([1, 2, 4, 5, 6, 8, 9, 16, 45, 59, 95, 234, 546, 646], 45))