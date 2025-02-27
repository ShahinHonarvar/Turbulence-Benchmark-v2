def all_left_truncatable_prime(numbers):

    def is_prime(n, primes):
        if n < 2:
            return False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        n_str = str(n)
        while n_str:
            n = int(n_str)
            if not is_prime(n, primes):
                return False
            n_str = n_str[:-1]
        return True
    x = numbers[73]
    primes = [2]
    prime_candidates = [str(num) for num in range(2, x)]
    left_truncatable_primes = []
    for prime_candidate in prime_candidates:
        if prime_candidate not in primes and is_left_truncatable(int(prime_candidate), primes):
            primes.append(int(prime_candidate))
        if int(prime_candidate) > x:
            break
    return sorted([p for p in primes if is_left_truncatable(p, primes)], reverse=True)