def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    prime_factors = set()
    number = numbers[72]
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_factors.add(i)
    return prime_factors