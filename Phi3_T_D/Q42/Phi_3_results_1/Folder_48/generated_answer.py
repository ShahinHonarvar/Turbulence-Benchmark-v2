import heapq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) <= 247:
        number = numbers[247]
    else:
        number = numbers[247]
        numbers = numbers[:247] + numbers[248:]
    prime_factors_set = set()
    divisor = 2
    while number >= 2:
        if number % divisor == 0 and is_prime(divisor):
            prime_factors_set.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return prime_factors_set