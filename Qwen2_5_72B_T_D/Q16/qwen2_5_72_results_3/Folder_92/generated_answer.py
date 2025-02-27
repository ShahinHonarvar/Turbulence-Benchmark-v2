def sum_even_ints_inclusive(nums):
    even_sum = sum((num for num in nums[:2] if num % 2 == 0))
    return even_sum