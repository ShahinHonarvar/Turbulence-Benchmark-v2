from math import sqrt

def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    composites = {num for num in nums[314:348] if is_composite(num)}
    return composites