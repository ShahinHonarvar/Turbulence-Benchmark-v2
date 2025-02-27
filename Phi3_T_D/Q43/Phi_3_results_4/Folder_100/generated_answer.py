from math import sqrt

def find_primes_between_indices(nums):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    result = [num for i, num in enumerate(nums) if is_prime(num) and 25 <= i <= 62]
    return sorted(result)