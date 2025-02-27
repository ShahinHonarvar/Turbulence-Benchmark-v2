def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, sieve):
        if n == 0:
            return True
        nstr = str(n)
        if not is_prime(int(nstr)):
            return False
        if len(nstr) == 1:
            return n != 0
        return is_left_truncatable_prime(int(nstr[1:]), sieve)
    x = numbers[71]
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p, sieve)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes