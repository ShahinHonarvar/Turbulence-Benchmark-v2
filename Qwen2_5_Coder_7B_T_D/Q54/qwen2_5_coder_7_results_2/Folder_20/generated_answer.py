def all_right_truncatable_prime(nums):
    x = nums[100]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in range(11, x, 2):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
            if is_right_truncatable_prime(num):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True