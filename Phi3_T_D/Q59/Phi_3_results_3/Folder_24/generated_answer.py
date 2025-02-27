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

def is_left_truncatable_prime(p, primes):
    while p:
        if not is_prime(p):
            return False
        p = int(str(p)[:-1])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[65]
    prime_list = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [p for p in prime_list if is_left_truncatable_prime(p, prime_list)]
    return sorted(left_truncatable_primes, reverse=True)