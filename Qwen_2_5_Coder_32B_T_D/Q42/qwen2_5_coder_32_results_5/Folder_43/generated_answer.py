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
        for i in range(2, n + 1):
            while n % i == 0:
                result.add(i)
                n //= i
        return result
    target = numbers[29]
    return factors(target) if 0 <= 29 < len(numbers) else set()