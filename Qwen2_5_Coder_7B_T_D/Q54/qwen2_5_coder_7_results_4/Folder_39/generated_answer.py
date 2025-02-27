def all_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if all((int(temp) % i != 0 for i in range(2, int(int(temp) ** 0.5) + 1))):
                temp //= 10
            else:
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)