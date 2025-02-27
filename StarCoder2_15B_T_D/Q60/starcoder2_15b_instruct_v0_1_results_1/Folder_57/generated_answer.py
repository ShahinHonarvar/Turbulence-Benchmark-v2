def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 9:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
        n = int(str(n)[:-1])
    return is_prime(n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    x = x[54]
    left_right_truncatable_primes = []
    for n in range(1, x + 1):
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes