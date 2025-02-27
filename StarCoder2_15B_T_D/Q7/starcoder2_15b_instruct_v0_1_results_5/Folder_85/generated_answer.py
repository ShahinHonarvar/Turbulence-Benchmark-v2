def all_even_ints_inclusive(nums):
    return [n for i, n in enumerate(nums) if i in range(6, 9) and n % 2 == 0]