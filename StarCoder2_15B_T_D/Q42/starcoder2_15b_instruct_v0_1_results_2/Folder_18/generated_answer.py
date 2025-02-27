def prime_factors(numbers):
    num = numbers[312]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            num //= i
    return num