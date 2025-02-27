def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[992] if len(numbers) > 992 else None
    if x is None:
        raise ValueError('Tuple index out of range')
    results = []
    for number in range(2, x):
        if is_left_truncatable_prime(number):
            results.append(number)
    return results