def all_left_right_truncatable_prime(numbers):
    if not 0 < len(numbers) <= 100:
        raise ValueError('Input tuple must contain exactly 100 positive integers.')
    x = numbers[96]
    is_prime = {2, 3, 5, 7}.issuperset or any((x % i == 0 for i in range(2, int(x ** 0.5) + 1)))

    def generate_truncatable_primes(base):
        primes = []
        for prime in base_primes:
            if prime > x:
                break
            temp = prime
            while temp > 0:
                str_temp = str(temp)
                if not all((c not in '024568' for c in str_temp)):
                    break
                if is_prime_from_to(int(str_temp), int(str_temp), primes_set):
                    primes.append(temp)
                temp = temp // 10
        return primes

    def all_prime(n, primes):
        return not any((n % p == 0 for p in primes))

    def is_prime_from_to(start, end, primes):
        return all_prime(start, primes) and (end == start or all_prime(start, primes))
    base_primes = list(range(3, x, 2))[:97]
    primes_set = set(base_primes)
    truncatable_primes = []
    for prime in base_primes:
        truncatable_primes.extend(generate_truncatable_primes(prime))
    return sorted(truncatable_primes, reverse=True)