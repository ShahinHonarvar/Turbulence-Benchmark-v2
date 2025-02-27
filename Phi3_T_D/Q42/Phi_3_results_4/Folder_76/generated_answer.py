def prime_factors(numbers):

    def factors(n):
        result = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                result.add(i)
                n //= i
        if n > 1:
            result.add(n)
        return result
    if len(numbers) > 537:
        return factors(numbers[537])
    else:
        raise IndexError('List has less than 538 elements')