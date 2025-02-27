def prime_factors(numbers):
    index = 733
    if index < len(numbers):
        n = numbers[index]
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    else:
        return 'Index out of bounds'