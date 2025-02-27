def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and i >= 2 and (i <= 2):
            primes.append(num)
    primes.sort()
    return primes