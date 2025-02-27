def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(prime, primes_set):
    while prime > 0:
        if prime not in primes_set:
            return False
        prime //= 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) != 28:
        raise ValueError('Expected a tuple with 28 elements.')
    x = numbers[28]
    primes = set()
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num, primes):
            right_truncatable_primes.append(num)
            primes.update(str(num))
    return sorted(right_truncatable_primes)