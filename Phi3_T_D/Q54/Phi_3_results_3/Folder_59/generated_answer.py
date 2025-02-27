def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    if n not in primes_set:
        return False
    return all((is_right_truncatable_prime(n // 10, primes_set) for n in range(n, 0, -1)))

def all_right_truncatable_prime(numbers):
    x = numbers[84]
    primes_set = {2, 3, 5, 7}
    for i in range(7, x):
        if is_prime(i):
            primes_set.add(i)
    return sorted((n for n in primes_set if is_right_truncatable_prime(n, primes_set)), reverse=True)