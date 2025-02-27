def all_right_truncatable_prime(t):
    x = t[41]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    primes = [2]
    for num in range(3, x, 2):
        if is_prime(num):
            primes.append(num)
            if is_right_truncatable(num, primes):
                yield num