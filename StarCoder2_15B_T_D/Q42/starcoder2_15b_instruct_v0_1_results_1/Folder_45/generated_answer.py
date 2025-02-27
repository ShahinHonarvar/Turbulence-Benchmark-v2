def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    number_at_index_33 = numbers[33]
    for i in range(2, number_at_index_33 + 1):
        if number_at_index_33 % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set