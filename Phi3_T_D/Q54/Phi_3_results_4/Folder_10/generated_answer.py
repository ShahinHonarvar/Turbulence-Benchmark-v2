def all_right_truncatable_prime(numbers):
    x = numbers[38]
    is_prime = lambda n: n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def generate_right_truncatable_primes(n):
        str_n = str(n)
        prime_digits = [2, 3, 5, 7]
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in prime_digits:
                return False
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [p for p in primes if generate_right_truncatable_primes(p)]
    return sorted(right_truncatable_primes, reverse=True)