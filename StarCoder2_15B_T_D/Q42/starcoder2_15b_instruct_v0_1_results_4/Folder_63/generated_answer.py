def prime_factors(numbers):
    number = numbers[57]
    for i in range(2, number + 1):
        while number % i == 0:
            primes.append(i)
            number //= i
    return set(primes)