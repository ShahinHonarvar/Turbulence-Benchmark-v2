def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    for num in numbers:
        temp_num = num
        for i in range(2, temp_num + 1):
            while temp_num % i == 0 and is_prime(i):
                factors.add(i)
                temp_num //= i
    return factors