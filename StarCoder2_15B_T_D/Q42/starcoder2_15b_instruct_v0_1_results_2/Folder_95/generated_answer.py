def prime_factors(numbers):
    return set((factor for i in range(2, numbers[87] + 1) if numbers[87] % i == 0))