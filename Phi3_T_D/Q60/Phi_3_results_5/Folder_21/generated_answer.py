def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
                return False
        return True
    x = numbers[175]
    primes = set([2, 3])
    for i in range(5, x + 1):
        if is_prime(i):
            primes.add(i)
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime, primes) and prime <= x:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)