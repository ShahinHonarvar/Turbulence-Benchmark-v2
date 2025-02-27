def all_right_truncatable_prime(t):
    x = t[49]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num >= 10:
                num //= 10
                if not is_prime(num):
                    break
            else:
                primes.append(i)
    return sorted(primes)