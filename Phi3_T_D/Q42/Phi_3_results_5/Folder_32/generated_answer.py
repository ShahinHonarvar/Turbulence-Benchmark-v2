def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of_number(num):
        factors = set()
        divisor = 2
        while num > 1:
            if num % divisor == 0 and is_prime(divisor):
                factors.add(divisor)
                num //= divisor
            else:
                divisor += 1
        return factors
    index = 849
    if index < len(numbers):
        return prime_factors_of_number(numbers[index])
    else:
        return 'Index out of range.'