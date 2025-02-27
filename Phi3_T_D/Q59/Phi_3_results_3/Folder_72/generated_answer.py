def all_left_truncatable_prime(numbers):
    x = numbers[31]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n, sieve):
        str_n = str(n)
        for i in range(len(str_n)):
            if not sieve.get(int(str_n[i:])):
                return False
        return True
    sieve = [True] * x
    for i in range(2, x):
        if sieve[i]:
            for j in range(i * 2, x, i):
                sieve[j] = False
    left_truncatable_primes = [n for n in range(23, x) if is_left_truncatable_prime(n, sieve)]
    return sorted(left_truncatable_primes, reverse=True)