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

def all_right_truncatable_primes(numbers):
    if len(numbers) < 24 or not isinstance(numbers[24], int):
        raise ValueError('The tuple must contain at least 25 positive integers.')
    x = numbers[24]
    base_primes = [2, 3, 5, 7]

    def truncatable(prime, limit, base_primes):
        str_prime = str(prime)
        while str_prime:
            if not is_prime(int(str_prime)):
                return False
            str_prime = str_prime[:-1]
        return int(str_prime) > 1
    truncatable = [prime for prime in range(2, x) if prime in base_primes or truncatable(prime, x, base_primes)]
    return sorted(truncatable)