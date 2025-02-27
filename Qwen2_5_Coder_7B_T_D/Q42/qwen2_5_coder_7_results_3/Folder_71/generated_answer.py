def prime_factors(numbers):
    factors = set()
    for num in numbers:
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
    return factors if 78 < len(numbers) else None