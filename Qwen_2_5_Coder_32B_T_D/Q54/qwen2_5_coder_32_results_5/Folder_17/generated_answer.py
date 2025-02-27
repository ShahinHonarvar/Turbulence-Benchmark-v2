def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    right_trunc_primes = []
    for num in range(2, x):
        n = num
        while n > 0 and is_prime(n):
            n //= 10
        if n == 0:
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)