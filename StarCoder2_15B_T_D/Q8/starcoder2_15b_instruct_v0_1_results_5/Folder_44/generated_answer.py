def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 81 and i < 86 and (num % 2 == 0)]