from math import sqrt

def composite_nums_between_indices(nums):
    composite_set = set()

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False
    if len(nums) < 67:
        return composite_set
    for num in nums[10:67]:
        if is_composite(num):
            composite_set.add(num)
    return composite_set