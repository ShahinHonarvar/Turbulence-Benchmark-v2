def prime_factors(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(number):
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
    if len(num_list) > 92:
        number_at_index_92 = num_list[92]
        return get_prime_factors(number_at_index_92)
    else:
        raise IndexError('The list does not have an element at index 92.')