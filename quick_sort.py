def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if pivot > arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[end] = arr[end], arr[i]

    # pozícia pivotu
    return i


def quick_sort(arr, start, end):
    # base case
    if start >= end:
        return

    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

    return arr


arr = [1, 5, 3, 2, 9, 934, 2, 56, 34, 7, 0, 9]
print(quick_sort(arr, 0, len(arr) - 1))
