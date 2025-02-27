from math import sqrt

def composite_nums_between_indices(nums):
    return {num for num in nums[68:87] if num > 1 and any((num % i == 0 for i in range(2, int(sqrt(num)) + 1)))}