def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    sieve = [True] * (x + 1)
    p = 2
    while p * p <= x:
        if sieve[p]:
            for i in range(p * p, x + 1, p):
                sieve[i] = False
        p += 1
    primes = [p for p in range(2, x + 1) if sieve[p]]

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not (int(s[i:]) in primes and int(s[:-i]) in primes):
                return False
        return True
    return [p for p in primes if is_truncatable_prime(p)]