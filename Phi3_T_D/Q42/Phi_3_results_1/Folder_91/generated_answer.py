def prime_factors(numbers):
    number_to_factors = {}
    for number in numbers:
        factors = {}
        divisor = 2
        while divisor * divisor <= number:
            while number % divisor == 0:
                factors[divisor] = factors.get(divisor, 0) + 1
                number //= divisor
            divisor += 1
        if number > 1:
            factors[number] = factors.get(number, 0) + 1
        number_to_factors[number] = factors
    return set(number_to_factors.get(numbers[6], {}).keys())