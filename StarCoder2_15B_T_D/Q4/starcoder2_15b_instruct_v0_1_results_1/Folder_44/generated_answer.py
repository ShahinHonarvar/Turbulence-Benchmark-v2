def all_pos_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise TypeError('Invalid input type')
    pos_ints = []
    for i, num in enumerate(nums):
        if 81 <= i < 86 and num > 0:
            pos_ints.append(num)
    return pos_ints