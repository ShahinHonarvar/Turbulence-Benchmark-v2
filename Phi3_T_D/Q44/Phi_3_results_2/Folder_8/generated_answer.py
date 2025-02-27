from math import sqrt

def composite_nums_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return {num for num in nums[68:87] if not is_prime(num)}