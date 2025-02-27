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

def all_left_right_truncatable_prime(primes_range):
    x = primes_range[975]

    def is_left_right_truncatable_prime(prime):
        if not (str(prime).startswith('1') or str(prime).startswith('2')):
            return False
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:i])):
                return False
        return True
    all_truncatable_primes = [p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)]
    return all_truncatable_primes[::-1]