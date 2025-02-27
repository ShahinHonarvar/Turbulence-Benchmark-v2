def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 8 and i <= 9 and (num % 2 == 0)]