def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 100 and i < 102 and (num % 2 == 0)]