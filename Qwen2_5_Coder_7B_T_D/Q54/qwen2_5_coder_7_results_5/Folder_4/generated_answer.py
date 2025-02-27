def all_right_truncatable_prime(numbers):
    x = numbers[96]
    primes = set()
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    right_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if any((temp % i == 0 for i in range(2, int(temp ** 0.5) + 1))):
                break
            temp //= 10
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)