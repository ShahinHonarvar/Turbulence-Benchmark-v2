def all_neg_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise TypeError('Argument must be a list of integers')
    negative_ints = []
    for i, num in enumerate(nums):
        if i >= 38 and i < 52 and (num < 0):
            negative_ints.append(num)
    return negative_ints