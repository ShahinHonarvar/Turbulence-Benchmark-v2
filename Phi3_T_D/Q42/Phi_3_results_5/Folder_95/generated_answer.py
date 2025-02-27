def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) < 88:
        return 'Invalid input'
    num = numbers[87]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
        if divisor * divisor > num:
            if num > 1:
                factors.add(num)
            break
    return factors