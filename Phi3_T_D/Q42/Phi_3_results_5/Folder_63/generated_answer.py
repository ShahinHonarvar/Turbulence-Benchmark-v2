def prime_factors(integers_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    number = integers_list[57]
    for i in range(2, number + 1):
        while number % i == 0 and is_prime(i):
            factors.add(i)
            number //= i
    return factors