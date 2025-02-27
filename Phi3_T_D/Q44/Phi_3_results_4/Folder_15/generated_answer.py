from math import sqrt

def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False
    return set(filter(is_composite, nums[0:4]))