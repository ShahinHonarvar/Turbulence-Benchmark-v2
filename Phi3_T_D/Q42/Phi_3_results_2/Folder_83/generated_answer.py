def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(numbers):
    if not numbers or len(numbers) < 96:
        return None
    n = numbers[95]
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(n // i):
                factors.add(n // i)
    return factors