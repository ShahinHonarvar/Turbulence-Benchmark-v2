def prime_factors(numbers):
    prime_factors = set()
    number = numbers[74]
    for i in range(2, number + 1):
        if is_prime(i):
            prime_factors.add(i)
    return prime_factors

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True