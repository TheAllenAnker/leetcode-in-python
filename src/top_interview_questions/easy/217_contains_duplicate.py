def contains_duplicate(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        else:
            nums_set.add(num)
    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
