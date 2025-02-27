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

    def factors(n):
        result = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                if is_prime(i):
                    result.add(i)
                result.update(factors(n // i))
        if is_prime(n):
            result.add(n)
        return result
    return factors(numbers[453])