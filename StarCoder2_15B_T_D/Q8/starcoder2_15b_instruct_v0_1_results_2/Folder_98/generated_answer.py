def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i % 2 == 0 and 0 < i < 6]