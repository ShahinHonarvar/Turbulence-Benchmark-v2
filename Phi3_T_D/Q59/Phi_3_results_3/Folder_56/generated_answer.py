def all_left_truncatable_prime(tup):
    primes = []
    is_prime = lambda n: n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def generate_primes(start, seq):
        if start >= tup[30]:
            return
        num = start
        while num > 0:
            if is_prime(num):
                seq.append(num)
            num //= 10
    for i in range(10, int(tup[30] ** 0.5) + 1):
        generate_primes(i, primes)
    return sorted(primes)