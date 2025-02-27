def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(p, primes_set):
        str_p = str(p)
        return all((is_prime(int(str_p[:len(str_p) - i])) for i in range(len(str_p)))) and p in primes_set
    truncatable_primes = []
    x = numbers[69]
    for p in range(2, x):
        if is_prime(p):
            prime_str = str(p)
            for i in range(len(prime_str)):
                if not is_right_truncatable_prime(int(prime_str[:len(prime_str) - i - 1]), {p}.union(truncatable_primes)):
                    break
            else:
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)