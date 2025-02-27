def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0:
                result.add(i)
        return result
    number = numbers[2]
    all_factors = factors(number)
    prime_factor_set = {factor for factor in all_factors if is_prime(factor)}
    return prime_factor_set