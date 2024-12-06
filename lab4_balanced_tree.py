class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    if node is None:
        return True
    lh = height(node.left)
    rh = height(node.right)
    if abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False

if __name__ == "__main__":
    print("Введите последовательность целых чисел, оканчивающихся нулём, через пробел:")
    data = list(map(int, input().split()))

    data.pop()

    root = None
    print("Является ли дерево сбалансированным:")
    for num in data:
        root = insert(root, num)

    if is_balanced(root):
        print("YES")
    else:
        print("NO")