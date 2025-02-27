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

def all_right_truncatable_prime(tup):
    x = tup[55]
    primes = []

    def right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for num in range(2, x):
        if right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)