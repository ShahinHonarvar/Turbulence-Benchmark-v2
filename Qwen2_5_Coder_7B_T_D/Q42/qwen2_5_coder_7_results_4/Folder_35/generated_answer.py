from math import sqrt

def prime_factors(numbers):
    result = set()
    num = numbers[993]
    while num % 2 == 0:
        result.add(2)
        num //= 2
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            result.add(i)
            num //= i
    if num > 2:
        result.add(num)
    return result