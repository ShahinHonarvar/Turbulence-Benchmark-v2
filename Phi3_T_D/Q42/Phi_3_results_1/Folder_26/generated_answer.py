def prime_factors(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return {i for i in range(2, n + 1) if n % i == 0 and is_prime(i)}
    number = int_list[222] if len(int_list) > 222 else None
    return factors(number) if number else set()