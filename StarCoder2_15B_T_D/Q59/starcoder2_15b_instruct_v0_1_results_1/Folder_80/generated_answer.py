def all_left_truncatable_prime(tup):
    x = tup[14]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and (not contains_zero(i)):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def contains_zero(num):
    while num > 0:
        if num % 10 == 0:
            return True
        num //= 10
    return False