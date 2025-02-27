def all_right_truncatable_prime(tup):
    right_truncatable_primes = []
    x = tup[81]
    for i in range(1, x):
        if is_prime(i):
            if is_right_truncatable_prime(i):
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True