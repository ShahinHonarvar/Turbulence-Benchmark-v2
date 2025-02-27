def prime_factors(numbers):

    def factors(n):
        result = set()
        while n % 2 == 0:
            result.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                result.add(i)
                n //= i
        if n > 2:
            result.add(n)
        return result
    return factors(numbers[63])