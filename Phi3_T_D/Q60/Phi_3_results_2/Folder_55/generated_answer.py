def all_left_right_truncatable_prime(numbers):

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_eligible(n: int, prefixes: set, suffixes: set) -> bool:
        while n > 0:
            if not is_prime(n):
                return False
            if n not in prefixes or n not in suffixes:
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    x = numbers[73]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = []
    prefixes, suffixes = (set(), set())
    for prime in primes:
        if is_eligible(prime, prefixes, suffixes):
            truncatable_primes.append(prime)
            prefixes.add(prime // 10 ** (len(str(prime)) - 1))
            suffixes.add(prime % 10)
    return sorted(truncatable_primes, reverse=True)