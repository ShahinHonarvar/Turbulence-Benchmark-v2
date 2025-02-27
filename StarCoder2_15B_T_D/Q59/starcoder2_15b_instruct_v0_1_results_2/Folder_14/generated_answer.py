def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[0]
    left_truncatable_primes = [n for n in range(2, x) if is_prime(n)]
    for i in range(78):
        left_truncatable_primes = [n for n in left_truncatable_primes if is_prime(n) and n % 10 != 0]
    return sorted(left_truncatable_primes, reverse=True)