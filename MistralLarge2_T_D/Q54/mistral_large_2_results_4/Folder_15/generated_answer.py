def is_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(tup):
    x = tup[6]
    primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(primes, reverse=True)