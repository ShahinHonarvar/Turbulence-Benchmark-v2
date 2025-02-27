def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    return sorted([n for i, n in enumerate(numbers) if is_prime(n) and 61 <= i <= 79])