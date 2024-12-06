def bubbleSort(arr):

    for n in range(len(arr) - 1, 0, -1):

        swapped = False  

        for i in range(n):
            if arr[i] > arr[i + 1]:

                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                swapped = True

        if not swapped:
            break
print("Введите целые числа через пробел:")
arr = list(map(int, input().strip().split()))
print("Несортированный список:")
print(arr)

bubbleSort(arr)

print("Сортированный список:")
print(arr)