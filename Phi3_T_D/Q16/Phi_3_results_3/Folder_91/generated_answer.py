def sum_even_ints_inclusive(nums):
    even_sum = sum((n for n in nums[:6] if n % 2 == 0))
    return even_sum