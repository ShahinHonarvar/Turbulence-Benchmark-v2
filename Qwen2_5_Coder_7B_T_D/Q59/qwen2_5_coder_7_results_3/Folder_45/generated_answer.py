def all_left_truncatable_prime(numbers):
    x = numbers[61]
    primes = []
    for num in range(2, x):
        if all((int(prime) != 0 for prime in str(num))) and all((all((int(num[:i]) % 2 != 0 for i in range(1, len(num) + 1))) for num in str(num))):
            primes.append(num)
    return sorted(primes)