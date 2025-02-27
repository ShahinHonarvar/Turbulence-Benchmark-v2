def all_right_truncatable_prime(numbers):

    def is_prime(n, sieve=None):
        if sieve is None:
            sieve = [True] * (n + 1)
        if n < 2 or sieve[n] == False:
            return n == 2
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        sieve[n] = False
        return True

    def all_right_truncatable_primes_less_than(n):

        def is_right_truncatable(n):
            str_n = str(n)
            for i in range(len(str_n)):
                part = int(str_n[i:])
                if not is_prime(part):
                    return False
            return True
        right_truncatable_primes = []
        for i in range(2, n):
            if is_right_truncatable(i):
                right_truncatable_primes.append(i)
        return right_truncatable_primes
    tail = numbers[50]
    return sorted(all_right_truncatable_primes_less_than(tail), reverse=True)