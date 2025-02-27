def all_right_truncatable_prime(numbers):
    target = numbers[46]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if not is_prime(n):
            return False
        return all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1) if n // 10 ** (len(str(n)) - i) in primes))
    primes = {2}
    right_truncatable_primes = []
    current = 11
    while current < target:
        if is_right_truncatable_prime(current, primes):
            right_truncatable_primes.append(current)
        current += 1
        while current not in primes and current < target:
            for prime in list(primes):
                primes.add(prime * 10 + current % 10)
            current += 1
    return sorted(right_truncatable_primes, reverse=True)