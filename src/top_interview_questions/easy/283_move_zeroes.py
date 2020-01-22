def move_zeroes(nums):
    non_zero_ends_at = -1
    curr = 0
    while curr < len(nums):
        if nums[curr] != 0:
            nums[non_zero_ends_at + 1], nums[curr] = nums[curr], nums[non_zero_ends_at + 1]
            non_zero_ends_at += 1
        curr += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)
