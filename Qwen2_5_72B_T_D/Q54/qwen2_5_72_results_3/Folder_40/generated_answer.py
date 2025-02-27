def all_right_truncatable_prime(numbers):
    x = numbers[10]
    primes = []
    for num in range(2, x):
        if all((num % d != 0 for d in range(2, int(num ** 0.5) + 1))):
            if all((int(str(num)[:-i]) in primes for i in range(1, len(str(num))))):
                primes.append(num)
    return sorted(primes, reverse=True)