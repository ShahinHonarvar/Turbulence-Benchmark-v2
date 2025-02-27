def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = t[803]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if is_truncatable_prime(num, primes):
            primes.append(num)
    primes_less_than_x = [p for p in primes if p < x]
    return primes_less_than_x