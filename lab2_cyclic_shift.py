def find_min_shift(s, t):

    if len(s) != len(t):
        return -1

    double_s = s * 2

    pos = double_s.find(t)

    if pos != -1:
        return len(s) - pos
    else:
        return -1

print("Введите первую строку:")
s = input()

print("Введите вторую строку:")
t = input()

print("Размер циклического сдвига")
print(find_min_shift(s, t))