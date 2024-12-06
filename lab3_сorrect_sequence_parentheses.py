def parentheses_to_delete(s):
    stack = []
    deletions = 0
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                deletions += 1
    deletions += len(stack)
    
    return deletions

print("Введите последовательностьскобок:")
s = input()

print("Требуется удалить символов:\n", parentheses_to_delete(s))