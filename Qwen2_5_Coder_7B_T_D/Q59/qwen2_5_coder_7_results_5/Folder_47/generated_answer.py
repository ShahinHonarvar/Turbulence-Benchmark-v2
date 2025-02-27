def all_left_truncatable_prime(t):
    x = t[49]
    primes = set()

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

    def left_truncatable(n):
        while n > 0:
            if n in primes:
                n //= 10
            else:
                return False
        return True
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num):
            primes.add(num)
            if left_truncatable(num):
                primes.add(num)
    return sorted(list(primes))