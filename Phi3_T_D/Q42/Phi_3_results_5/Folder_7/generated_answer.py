def prime_factors(numbers):

    def prime_factors_of_single(number):
        factors = set()
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factors.add(divisor)
                number //= divisor
            divisor += 1
            if divisor * divisor > number and number > 1:
                factors.add(number)
                break
        return factors
    index = 851
    if index < len(numbers):
        return prime_factors_of_single(numbers[index])
    else:
        return set()