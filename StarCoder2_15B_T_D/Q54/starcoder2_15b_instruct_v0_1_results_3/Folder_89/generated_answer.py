import math

def all_right_truncatable_prime(nums):
    x = nums[97]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        j = i
        while j > 0:
            if not is_right_truncatable_prime(j):
                break
            j //= 10
        if j == 0:
            result.append(i)
    result.sort(reverse=True)
    return result