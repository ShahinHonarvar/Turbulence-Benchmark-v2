def sum_even_ints_inclusive(nums):
    return sum((n for n in nums if n % 2 == 0 and 0 <= nums.index(n) <= 0))