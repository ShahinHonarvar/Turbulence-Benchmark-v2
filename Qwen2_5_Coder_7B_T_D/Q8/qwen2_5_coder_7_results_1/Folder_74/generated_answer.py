def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 13 < i < 70 and num % 2 == 0]