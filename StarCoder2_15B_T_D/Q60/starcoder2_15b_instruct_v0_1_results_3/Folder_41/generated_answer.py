def is_truncatable_prime(n, primes):
    if n < 2:
        return False
    if n in primes:
        return True
    if n % 2 == 0 or str(n).endswith('0'):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    if is_truncatable_prime(int(str(n)[1:]), primes) and is_truncatable_prime(int(str(n)[:-1]), primes):
        primes.add(n)
        return True
    return False

def all_left_right_truncatable_prime(nums):
    primes = set()
    truncatable_primes = []
    for n in nums:
        if is_truncatable_prime(n, primes):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)