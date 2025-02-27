def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[14]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n):
        return False
    return is_truncatable_prime(n // 10)