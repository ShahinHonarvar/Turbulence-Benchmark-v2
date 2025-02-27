from math import sqrt

def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums[20:201]) if n < 2 or any((n % i == 0 for i in range(2, int(sqrt(n)) + 1)))}