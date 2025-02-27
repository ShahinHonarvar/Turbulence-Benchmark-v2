from math import sqrt

def composite_nums_between_indices(nums):
    start, end = (23, 23)

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {n for n in nums[start:end + 1] if is_composite(n)}