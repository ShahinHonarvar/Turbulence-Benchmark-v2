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

def is_truncatable_prime(n, primes_set):
    str_n = str(n)
    for p in [str_n[1:], str_n[:-1]]:
        if not is_prime(int(p)) or int(p) not in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[57]
    primes = set(filter(is_prime, range(2, x + 1)))
    truncatable_primes = [n for n in primes if is_truncatable_prime(n, primes)]
    return sorted(truncatable_primes, reverse=True)