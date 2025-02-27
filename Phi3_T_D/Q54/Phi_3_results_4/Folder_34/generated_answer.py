def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n, prime_digits):
    while n > 0:
        if not n in prime_digits or not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(nums):
    if not 18 <= len(nums) <= 20 or not all((isinstance(n, int) for n in nums)):
        raise ValueError('Argument must be a tuple of length between 18 and 20, containing positive integers.')
    if not is_prime(nums[18]):
        raise ValueError('Number at index 18 must be a prime.')
    prime_digits = {2, 3, 5, 7}
    truncatable_primes = []
    for i in range(1, nums[18]):
        if all(map(str.isdigit, str(i))) and is_right_truncatable_prime(i, prime_digits):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)