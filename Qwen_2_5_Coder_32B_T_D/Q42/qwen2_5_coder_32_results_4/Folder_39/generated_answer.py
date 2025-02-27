def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        return factors
    target_number = numbers[59]
    return get_factors(target_number)