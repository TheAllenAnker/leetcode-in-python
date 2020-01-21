def single_number(nums) -> int:
    """
    Return the number in the list that only appears once
    Tip: XOR operation
    :param nums: List[int]
    :return: int
    """
    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == '__main__':
    print(single_number([1, 1, 2, 3, 3, 4, 4]))
