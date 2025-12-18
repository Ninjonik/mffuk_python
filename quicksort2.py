array = [7, 3, 6, 5, 2, 9, 1, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = len(array) - 1

    left = []
    middle = []
    right = []

    for i in array:
        if i < pivot:
            left.append(i)
        if i == pivot:
            middle.append(i)
        if i > pivot:
            right.append(i)

    return quick_sort(left) + middle + quick_sort(right)


output = quick_sort(array)
print(output)