import math

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums: tuple) -> list:
    x = nums[18]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            is_truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_truncatable = False
                    break
                temp //= 10
            if is_truncatable:
                left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes