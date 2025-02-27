import math

def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for i, num in enumerate(numbers) if is_prime(num) and 23 <= i <= 75]
    return sorted(primes, reverse=True)