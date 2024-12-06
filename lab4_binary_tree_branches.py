class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def find_single_child_nodes(root, result):
    if root is not None:
        if (root.left is not None and root.right is None) or (root.left is None and root.right is not None):
            result.append(root.val)
        find_single_child_nodes(root.left, result)
        find_single_child_nodes(root.right, result)

def build_tree_and_find_single_child_nodes(sequence):
    sequence = sequence[:-1]

    root = None
    for num in sequence:
        root = insert(root, num)

    result = []
    find_single_child_nodes(root, result)

    result.sort()
    return result

print("Введите последовательность целых чисел, оканчивающихся нулём, через пробел:")
sequence = arr = list(map(int, input().split()))
single_child_nodes = build_tree_and_find_single_child_nodes(sequence)

print("Вершины, имеющие только одного ребёнка:")
for s in single_child_nodes:
    print(s)