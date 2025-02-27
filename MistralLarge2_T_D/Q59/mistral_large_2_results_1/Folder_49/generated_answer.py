def is_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n) or '0' in str(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(tup):
    x = tup[14]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)