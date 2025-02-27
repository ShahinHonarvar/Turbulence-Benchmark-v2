def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(primes, n):
        str_n = str(n)
        while str_n:
            if int(str_n) not in primes:
                return False
            str_n = str_n[1:-1]
        return True
    x = numbers[50]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1):
        if is_prime(i):
            primes.append(i)
    truncatable_primes = [p for p in primes if is_truncatable(primes, p)]
    return sorted(truncatable_primes, reverse=True)