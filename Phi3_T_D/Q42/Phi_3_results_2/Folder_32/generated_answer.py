def prime_factors(list_of_nums):
    num = list_of_nums[849]
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    return factors