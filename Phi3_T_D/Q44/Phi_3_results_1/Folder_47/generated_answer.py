from math import sqrt

def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        if n == 2:
            return False
        if n % 2 == 0:
            return True
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return True
        return False
    return {num for num in nums[75:89] if is_composite(num)}