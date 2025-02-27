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
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        return result
    target_number = numbers[537]
    all_factors = factors(target_number)
    prime_factors_set = {factor for factor in all_factors if is_prime(factor)}
    return prime_factors_set