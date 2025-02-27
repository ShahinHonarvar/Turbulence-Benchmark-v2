def all_left_truncatable_prime(primes):
    x = primes[73]
    left_truncatable = []

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

    def is_left_truncatable(n, primes_set):
        if n not in primes_set:
            return False
        str_num = str(n)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    primes_set = set(primes)
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i, primes_set):
            left_truncatable.append(i)
    return left_truncatable