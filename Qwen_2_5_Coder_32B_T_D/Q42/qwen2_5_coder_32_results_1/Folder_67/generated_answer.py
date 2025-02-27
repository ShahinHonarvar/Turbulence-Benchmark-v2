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
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        return result
    number = numbers[43]
    fact = factors(number)
    return {f for f in fact if is_prime(f)}