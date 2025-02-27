def is_prime(n):
    """
    Checks whether a number is prime.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    """
    Finds the sorted list of all prime numbers from index 46 to index 61, both inclusive.
    """
    primes = []
    for i, n in enumerate(numbers):
        if is_prime(n) and 46 <= i <= 61:
            primes.append(n)
    primes.sort()
    return primes