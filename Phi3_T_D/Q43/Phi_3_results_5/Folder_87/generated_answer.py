from math import sqrt

def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    start, end = (11, 41)
    primes = [num for num in numbers[start:end + 1] if is_prime(num)]
    return sorted(primes, reverse=True)