def prime_factors(list_of_integers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_prime_factors(number):
        factors = set()
        for i in range(2, number + 1):
            if is_prime(i) and number % i == 0:
                factors.add(i)
        return factors
    if len(list_of_integers) > 321:
        return get_prime_factors(list_of_integers[321])
    else:
        return set()