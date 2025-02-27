def prime_factors(numbers):
    return set(reduce(lambda x, y: x * y, [i for i in range(2, numbers[7] + 1) if numbers[7] % i == 0]))