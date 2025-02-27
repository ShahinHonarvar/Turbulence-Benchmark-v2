def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    number_at_78 = numbers[78]
    divisor = 2
    while number_at_78 > 1:
        if number_at_78 % divisor == 0 and is_prime(divisor):
            prime_factors_set.add(divisor)
            number_at_78 //= divisor
        else:
            divisor += 1
    return prime_factors_set