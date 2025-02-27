def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 100 <= i < 102 and num % 2 == 0]