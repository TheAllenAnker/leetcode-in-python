from lib.basic_data_structures import TreeNode


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    left = 1 + max_depth(root.left)
    right = 1 + max_depth(root.right)
    return max(left, right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    print(max_depth(root))
