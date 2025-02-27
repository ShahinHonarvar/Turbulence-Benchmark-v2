def all_neg_ints_exclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) for n in nums)):
        raise TypeError('Argument must be a list of integers')
    neg_ints = [n for n in nums if n < 0]
    return neg_ints[81:86]