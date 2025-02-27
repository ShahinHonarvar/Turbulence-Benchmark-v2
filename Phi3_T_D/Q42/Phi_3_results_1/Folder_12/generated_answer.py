from math import sqrt

def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime(i) and n % i == 0:
                result.add(i)
                while n % i == 0:
                    n //= i
        if is_prime(n):
            result.add(n)
        return result
    if len(nums) > 27:
        return factors(nums[27])
    else:
        raise IndexError('List does not have an element at index 27.')