def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:11]) if num % 2 == 0]