def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num_to_factor = numbers[43]
    factors = set()
    div = 2
    while num_to_factor > 1:
        while num_to_factor % div == 0:
            factors.add(div)
            num_to_factor //= div
        div += 1
    return factors