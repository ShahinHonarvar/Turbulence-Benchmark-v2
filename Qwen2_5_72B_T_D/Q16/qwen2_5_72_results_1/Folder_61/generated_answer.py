def sum_even_ints_inclusive(nums):
    return sum((num for num in nums[:8] if num % 2 == 0))