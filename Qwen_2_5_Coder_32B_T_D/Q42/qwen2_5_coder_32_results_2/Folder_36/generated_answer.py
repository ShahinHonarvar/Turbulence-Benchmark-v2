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
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                if is_prime(i):
                    result.add(i)
                num //= i
        if num > 1 and is_prime(num):
            result.add(num)
        return result
    if len(numbers) > 990:
        return factors(numbers[990])
    return set()