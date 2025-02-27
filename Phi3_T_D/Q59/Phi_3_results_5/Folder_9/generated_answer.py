def all_left_truncatable_prime(numbers):

    def is_prime(n, sieve):
        return n in sieve

    def gen_left_truncatable_primes(start, sieve):
        result = []
        while start < x:
            if is_prime(start, sieve):
                if all((is_prime(int(str(start)[i:]), sieve) for i in range(1, len(str(start))))):
                    result.append(start)
            start += 1
        return result
    x = numbers[29]
    sieve = {p for p in range(2, x) if is_prime(p, {})}
    truncatable_primes = gen_left_truncatable_primes(11, sieve)
    return sorted(truncatable_primes, reverse=True)