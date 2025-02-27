def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, stashed_primes):
        if n < 10:
            return n in stashed_primes[n]
        return n in stashed_primes[n % 10] and is_left_truncatable(n // 10, stashed_primes)
    primes = set((number for number in map(str, range(2, x)) if is_prime(int(number))))
    stashed_primes = {i: set() for i in range(10)}
    for prime in primes:
        stashed_primes[int(prime[-1])].add(int(prime))
        for i in range(len(prime) - 1):
            stashed_primes[int(prime[i])].add(int(prime[:i + 1]))
    return sorted((int(prime) for prime in primes if is_left_truncatable(int(prime), stashed_primes)))