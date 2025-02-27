def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 37:
        x = numbers[37]
    else:
        raise ValueError('Tuple size must be at least 38')
    if x < 11:
        return []
    truncatable_primes = []
    primes_set = {2, 3, 5, 7}
    for num in range(x - 1, 11, -1):
        if num in primes_set:
            if is_right_truncatable_prime(num, primes_set):
                truncatable_primes.append(num)
    return truncatable_primes