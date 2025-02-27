def all_left_right_truncatable_prime(range_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True

    def generate_primes(n):
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    x = range_tuple[88]
    primes = generate_primes(x)
    truncatable_primes = [prime for prime in primes if is_truncatable_prime(prime)]
    return sorted(truncatable_primes, reverse=True)