def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes_set):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_left_truncatable_prime(n // 10, primes_set)

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes_set = {2, 3, 5, 7}
    for i in range(10, x):
        if str(i) not in '024568':
            if is_left_truncatable_prime(i, primes_set):
                primes_set.add(i)
    return sorted(list(primes_set), reverse=True)