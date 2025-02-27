import math

def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        is_prime = True
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime and 295 <= i <= 455:
            primes.append(num)
    primes.sort(reverse=True)
    return primes