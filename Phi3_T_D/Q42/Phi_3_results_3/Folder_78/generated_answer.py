def prime_factors(integers):

    def prime_factors_of_single_number(number):
        factors = set()
        divisor = 2
        while divisor * divisor <= number:
            while number % divisor == 0:
                factors.add(divisor)
                number //= divisor
            divisor += 1
        if number > 1:
            factors.add(number)
        return factors
    if len(integers) > 91:
        return prime_factors_of_single_number(integers[91])
    else:
        raise ValueError('The list does not contain an integer at index 91.')