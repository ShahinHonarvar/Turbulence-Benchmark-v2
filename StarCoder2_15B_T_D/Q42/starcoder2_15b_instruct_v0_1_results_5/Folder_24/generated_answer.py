def prime_factors(integers):
    number = integers[74]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        prime_factors = []
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                prime_factors.append(i)
        return prime_factors
    return get_prime_factors(number)