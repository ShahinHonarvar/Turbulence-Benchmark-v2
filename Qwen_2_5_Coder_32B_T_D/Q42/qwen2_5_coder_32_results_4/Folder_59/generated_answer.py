def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0:
                result.add(i)
        return result
    num = numbers[2]
    all_factors = factors(num)
    prime_factor_set = {factor for factor in all_factors if is_prime(factor)}
    return prime_factor_set