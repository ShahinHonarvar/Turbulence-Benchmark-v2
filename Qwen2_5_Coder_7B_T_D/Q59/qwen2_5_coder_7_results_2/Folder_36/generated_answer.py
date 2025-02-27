def all_left_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    for num in range(2, x):
        if all((int(num) % 2 != 0 and int(num) % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        if all((int(prime[:i]) in primes and int(prime[:i]) % 2 != 0 and (int(prime[:i]) % i != 0) for i in range(1, len(prime)))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)