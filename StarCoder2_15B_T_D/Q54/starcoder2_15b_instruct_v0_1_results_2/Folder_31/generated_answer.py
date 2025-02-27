import math

def all_right_truncatable_prime(nums):
    x = nums[50]
    is_prime = [True] * x
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime[i]:
            right_truncatable_primes.append(i)
            if not is_right_truncatable_prime(i):
                break
    right_truncatable_primes.sort(reverse=True)

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not is_prime[num]:
                return False
            num //= 10
        return is_prime[num]
    return right_truncatable_primes