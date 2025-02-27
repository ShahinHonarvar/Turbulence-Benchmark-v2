def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i % 2 == 0 and 2 <= i < 7]