def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        prime_factors_set = set()
        divisor = 2
        while num > 1:
            while num % divisor == 0 and is_prime(divisor):
                prime_factors_set.add(divisor)
                num //= divisor
            divisor += 1
        return prime_factors_set
    try:
        index = 38
        if index < 0 or index >= len(numbers):
            raise IndexError('Index out of range')
        return get_prime_factors(numbers[index])
    except IndexError as e:
        return str(e)