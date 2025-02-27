def all_left_right_truncatable_prime(numbers):
    all_primes = set()
    truncatable_primes = []
    primes = [2, 3, 5, 7]

    def sieve(num):
        prime = [True] * (num + 1)
        p = 2
        while p ** 2 <= num:
            if prime[p]:
                for i in range(p ** 2, num + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, num) if prime[p]]

    def is_truncatable_prime(prime, primes):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not (int(str_prime[i:]) in primes and int(str_prime[:-i]) in primes):
                return False
        return True
    x = numbers[24]
    max_num = max(max(primes), 11)
    while max_num <= x:
        primes = sieve(max_num)
        k = len(truncatable_primes)
        for prime in primes:
            if prime not in all_primes and is_truncatable_prime(prime, all_primes):
                truncatable_primes.append(prime)
        all_primes.update(primes)
        max_num *= 10
    return sorted(truncatable_primes)