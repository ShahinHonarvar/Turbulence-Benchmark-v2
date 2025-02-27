import math

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = set()
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))):
            primes.add(num)
    right_truncatable = []
    for prime in primes:
        num = prime
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            right_truncatable.append(prime)
    return sorted(right_truncatable, reverse=True)