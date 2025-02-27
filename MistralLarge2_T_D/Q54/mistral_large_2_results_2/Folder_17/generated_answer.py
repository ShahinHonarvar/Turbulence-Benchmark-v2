def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[36]
    primes = []

    def is_right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    num = 2
    while num < x:
        if is_right_truncatable(num):
            primes.append(num)
        num += 1
    primes.sort(reverse=True)
    return primes