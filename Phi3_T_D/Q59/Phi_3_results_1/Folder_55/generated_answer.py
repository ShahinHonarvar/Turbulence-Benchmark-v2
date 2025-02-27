def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_primes(numbers):
    if len(numbers) < 74:
        raise ValueError('Tuple is too short. At least 74 elements required.')
    x = numbers[73]
    truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes