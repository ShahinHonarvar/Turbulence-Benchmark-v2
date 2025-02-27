def all_odd_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if i > 0 and i < 5 and (n % 2 != 0)]