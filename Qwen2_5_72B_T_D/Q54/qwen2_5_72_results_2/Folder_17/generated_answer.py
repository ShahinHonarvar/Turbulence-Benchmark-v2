def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    primes = []
    for num in range(2, x):
        if right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)