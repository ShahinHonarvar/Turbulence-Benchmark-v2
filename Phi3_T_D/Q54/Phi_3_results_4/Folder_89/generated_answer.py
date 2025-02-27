def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(prime, primes_set):
        return all((is_prime(int(str(prime)[:i])) for i in range(1, len(str(prime)))))
    x = numbers[97]
    primes_set = {p for p in range(x) if is_prime(p)}
    right_truncatables = [p for p in primes_set if is_right_truncatable(p, primes_set)]
    return sorted(right_truncatables, reverse=True)