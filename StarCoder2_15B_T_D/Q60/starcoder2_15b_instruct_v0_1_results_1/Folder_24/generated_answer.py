def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(x):
        if len(str(x)) <= 1:
            return False
        for i in range(len(str(x))):
            if i > 0:
                x //= 10
            if i < len(str(x)) - 1:
                x %= 10 ** (len(str(x)) - 1)
            if not is_prime(x):
                return False
        return True

    def is_prime(x):
        if x in (0, 1):
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    x = t[65]
    truncatable_primes = []
    for i in range(x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes