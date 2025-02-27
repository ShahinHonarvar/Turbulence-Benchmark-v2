def prime_factors(numbers):
    prime_factors_set = set()
    number_to_factor = numbers[848]
    divisor = 2
    while divisor ** 2 <= number_to_factor:
        if number_to_factor % divisor:
            divisor += 1
        else:
            number_to_factor //= divisor
            prime_factors_set.add(divisor)
    if number_to_factor > 1:
        prime_factors_set.add(number_to_factor)
    return prime_factors_set