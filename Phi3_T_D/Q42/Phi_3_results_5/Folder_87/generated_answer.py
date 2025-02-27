def prime_factors(numbers):
    if len(numbers) > 96:
        num = numbers[96]
    else:
        return 'Index out of range'

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n
    return set(factors(num))