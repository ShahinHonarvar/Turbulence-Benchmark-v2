def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes_set):
    if n not in primes_set:
        return False
    str_n = str(n)
    return all((is_left_truncatable_prime(int(str_n[i:]), primes_set) for i in range(1, len(str_n))))

def all_left_truncatable_prime(numbers):
    max_x = numbers[6]
    primes = set(filter(is_prime, range(2, max_x)))
    return [p for p in sorted(primes, reverse=True) if is_left_truncatable_prime(p, primes)]