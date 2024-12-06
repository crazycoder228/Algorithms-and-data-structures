def nearest_smaller(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = i

        stack.append(i)
    
    return ' '.join(map(str, result))

print("Введите количество элементов в массиве:")
n = int(input())
print("Введите числа:")
arr = list(map(int, input().split()))

print("Ближайшее справа меньшее число:\n", nearest_smaller(arr))