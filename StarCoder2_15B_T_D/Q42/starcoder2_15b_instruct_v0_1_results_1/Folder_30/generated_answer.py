def prime_factors(numbers):
    index = 94
    if len(numbers) <= index:
        return set()
    number = numbers[index]
    is_prime = [True] * (number + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, number + 1, i):
                is_prime[j] = False
    primes = [i for i in range(number + 1) if is_prime[i]]
    factors = set()
    for prime in primes:
        while number % prime == 0:
            factors.add(prime)
            number //= prime
    return factors