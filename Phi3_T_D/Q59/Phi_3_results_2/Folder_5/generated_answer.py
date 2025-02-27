def all_left_truncatable_prime(numbers):
    x = numbers[55]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(prime, primes_set):
        primes = [prime]
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) in primes_set:
                primes.append(int(str_prime[i:]))
        return primes
    truncatable_primes = [2, 3, 5, 7]
    for i in range(10, x):
        if is_prime(i):
            primes_set = set(truncatable_primes)
            truncatables = left_truncatable(i, primes_set)
            truncatable_primes.extend(truncatables)
    return sorted(set(truncatable_primes))