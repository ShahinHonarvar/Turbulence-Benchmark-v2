def all_neg_ints_exclusive(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert all((isinstance(n, int) for n in nums)), 'nums must be a list of integers'
    result = []
    for i, n in enumerate(nums):
        if n < 0 and 32 <= i < 99:
            result.append(n)
    return result