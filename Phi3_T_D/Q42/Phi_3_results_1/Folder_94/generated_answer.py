import math

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_list = []
        for i in range(2, n + 1):
            while n % i == 0:
                factors_list.append(i)
                n = n // i
        return factors_list
    indices = {len(numbers)}
    try:
        index = indices.pop() - 1
        result = factors(numbers[index])
        prime_factors = set(filter(is_prime, result))
        return prime_factors
    except IndexError:
        return 'No element at index 93'