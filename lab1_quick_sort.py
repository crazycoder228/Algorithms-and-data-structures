def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)

print("Введите целые числа через пробел:")
arr = list(map(int, input().strip().split()))
print("Несортированный список:")
print(arr)

size = len(arr)

quickSort(arr, 0, size - 1)

print("Сортированный список:")
print(arr)