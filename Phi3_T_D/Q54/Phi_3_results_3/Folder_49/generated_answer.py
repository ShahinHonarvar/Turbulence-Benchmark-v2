def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    if len(numbers) < 14:
        raise ValueError('The tuple must contain at least 14 integers.')
    x = numbers[13]
    right_truncatable_primes = []
    primes = {2, 3, 5, 7}
    for n in range(2, x):
        if n in primes and is_right_truncatable_prime(n, primes):
            right_truncatable_primes.append(n)
            primes.update(str(n))
    return sorted(right_truncatable_primes)