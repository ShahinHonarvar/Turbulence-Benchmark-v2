def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 50 < i < 200 and num % 2 == 0]