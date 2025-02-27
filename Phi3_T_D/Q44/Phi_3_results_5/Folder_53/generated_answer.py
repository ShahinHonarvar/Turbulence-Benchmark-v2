from math import sqrt

def composite_nums_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return not is_prime(n)
    composites = {num for num in nums[222:223] if is_composite(num)}
    return composites