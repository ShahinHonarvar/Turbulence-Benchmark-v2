def all_even_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if i > 36 and i < 52 and (n % 2 == 0)]