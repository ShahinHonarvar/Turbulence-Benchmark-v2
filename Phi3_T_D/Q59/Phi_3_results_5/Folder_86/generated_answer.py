def all_left_truncatable_prime(numbers):
    x = numbers[126]
    truncatable_primes = []

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

    def is_left_truncatable(n, primes_set):
        if not is_prime(n):
            return False
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) for i in range(len(str_n))))
    primes_set = set(filter(is_prime, range(2, x)))
    for prime in primes_set:
        if is_left_truncatable(prime, primes_set):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)