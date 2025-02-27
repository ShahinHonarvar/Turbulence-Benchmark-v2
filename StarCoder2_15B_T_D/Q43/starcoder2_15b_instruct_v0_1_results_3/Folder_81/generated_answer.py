def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i, n in enumerate(numbers):
        if is_prime(n) and 59 <= i <= 97:
            primes.append(n)
    primes.sort(reverse=True)
    return primes