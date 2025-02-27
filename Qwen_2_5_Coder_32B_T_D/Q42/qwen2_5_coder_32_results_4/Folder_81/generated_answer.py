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

    def factors(num):
        result = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                result.add(i)
        return result
    return factors(numbers[20])