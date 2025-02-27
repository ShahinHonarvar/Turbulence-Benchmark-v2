def sum_even_ints_inclusive(nums):
    return sum((x for x in nums[:5] if x % 2 == 0))