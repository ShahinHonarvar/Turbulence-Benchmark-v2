def prime_factors(integers_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    if 27 < len(integers_list) and isinstance(integers_list[27], int):
        return prime_factors_of(integers_list[27])
    else:
        raise IndexError('The list does not contain enough elements or the element at index 27 is not an integer.')