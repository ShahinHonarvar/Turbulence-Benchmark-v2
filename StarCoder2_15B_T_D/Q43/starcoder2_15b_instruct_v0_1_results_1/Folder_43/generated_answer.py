import math

def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for num in numbers[31:93] if is_prime(num)]
    return sorted(primes, reverse=True)