def prime_factors(num_list):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    number = num_list[46]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors