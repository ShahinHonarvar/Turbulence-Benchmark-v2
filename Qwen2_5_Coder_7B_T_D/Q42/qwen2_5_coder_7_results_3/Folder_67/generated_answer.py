def prime_factors(numbers):

    def factors(n):
        result = set()
        divisor = 2
        while n >= divisor ** 2:
            if n % divisor == 0:
                result.add(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            result.add(n)
        return result
    return factors(numbers[43])