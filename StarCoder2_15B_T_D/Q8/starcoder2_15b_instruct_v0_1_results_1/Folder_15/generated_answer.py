def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 0 and i < 3 and (num % 2 == 0)]