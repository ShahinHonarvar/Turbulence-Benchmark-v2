def prime_factors(numbers):
    return set(factors(numbers[54]))

def factors(n):
    result = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    if n > 1:
        result.add(n)
    return result