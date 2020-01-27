from lib.basic_data_structures import TreeNode


def helper(nums, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    node = TreeNode(nums[mid])
    node.left = helper(nums, start, mid - 1)
    node.right = helper(nums, mid + 1, end)
    return node


def convert_arr_to_bst(nums) -> TreeNode:
    head = helper(nums, 0, len(nums) - 1)
    return head


if __name__ == '__main__':
    print(convert_arr_to_bst([-10, -3, 0, 5, 9]).val)
