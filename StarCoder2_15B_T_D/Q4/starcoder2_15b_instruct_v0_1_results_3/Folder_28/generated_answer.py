def all_pos_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) for n in nums)):
        raise TypeError('Argument must be a list of integers.')
    result = []
    for i, num in enumerate(nums):
        if num > 0 and 20 < i < 51:
            result.append(num)
    return result