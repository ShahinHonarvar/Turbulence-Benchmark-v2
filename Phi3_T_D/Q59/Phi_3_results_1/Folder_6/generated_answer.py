def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, digits):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def generate_left_truncatable_primes(limit):
    primes = []
    for i in range(limit, 1, -1):
        if is_left_truncatable_prime(i, 74):
            primes.append(i)
    primes.reverse()
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    return generate_left_truncatable_primes(x)