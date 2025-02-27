import math

def prime_factors(numbers):
    number_at_index_23 = numbers[23]
    if number_at_index_23 == 2:
        return {2}
    sqrt = int(math.sqrt(number_at_index_23))
    for i in range(2, sqrt + 1):
        if number_at_index_23 % i == 0:
            return set(prime_factors(numbers, [i]) + prime_factors(numbers, [number_at_index_23 // i]))
    return {number_at_index_23}