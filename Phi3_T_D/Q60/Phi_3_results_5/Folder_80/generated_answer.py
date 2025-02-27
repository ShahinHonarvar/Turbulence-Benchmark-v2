def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    if n not in primes:
        return False
    for i in range(1, len(str(n))):
        if is_prime(int(str(n)[:i])) is False or is_prime(int(str(n)[-i:])) is False:
            return False
    return True

def left_right_truncatable_prime(max_value, primes):
    result = []
    for prime in sorted(primes, reverse=True):
        if prime > max_value:
            continue
        if is_truncatable_prime(prime, primes):
            result.append(prime)
            max_value = prime
    return result

def all_left_right_truncatable_prime(nums):
    primes = [n for n in range(2, nums[14] + 1) if is_prime(n)]
    return left_right_truncatable_prime(nums[14], primes)