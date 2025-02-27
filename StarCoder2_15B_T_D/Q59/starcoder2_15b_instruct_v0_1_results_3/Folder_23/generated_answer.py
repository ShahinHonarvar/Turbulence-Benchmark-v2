def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[77]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = [n for n in primes if all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))]
    return sorted(left_truncatable_primes, reverse=True)