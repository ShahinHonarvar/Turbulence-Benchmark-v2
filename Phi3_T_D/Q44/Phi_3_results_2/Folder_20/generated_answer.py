from math import sqrt

def composite_nums_between_indices(nums):

    def is_composite(n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in nums[74:96] if is_composite(num)}