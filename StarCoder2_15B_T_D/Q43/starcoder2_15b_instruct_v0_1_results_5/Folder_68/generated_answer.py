def find_primes_between_indices(numbers):
    """Find all prime numbers between indices 1 and 5 (inclusive) in a list of integers."""
    primes = []
    for i, num in enumerate(numbers):
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime and 1 <= i <= 5:
            primes.append(num)
    primes.sort()
    return primes