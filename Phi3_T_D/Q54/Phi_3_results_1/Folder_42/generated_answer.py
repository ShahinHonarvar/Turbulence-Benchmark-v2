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

def is_right_truncatable_prime(n, valid_primes):
    str_n = str(n)
    if len(str_n) == 1:
        return n in valid_primes
    return all((is_prime(int(str_n[:-i])) for i in range(1, len(str_n))))

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    valid_primes = [p for p in range(2, x) if is_prime(p)]
    right_truncatable_primes = [int(str(p)[i:]) for p in valid_primes for i in range(len(str(p)), 0, -1) if is_right_truncatable_prime(p, valid_primes)]
    return sorted(right_truncatable_primes, reverse=True)