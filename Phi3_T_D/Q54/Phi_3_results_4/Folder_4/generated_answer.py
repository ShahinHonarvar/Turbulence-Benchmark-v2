def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n, primes_set):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(int_tuple):
    x = int_tuple[96]
    right_truncatable_primes = []
    for num in range(x - 1, 7, -1):
        if is_right_truncatable(num, set(range(2, num))):
            right_truncatable_primes.append(num)
    return right_truncatable_primes