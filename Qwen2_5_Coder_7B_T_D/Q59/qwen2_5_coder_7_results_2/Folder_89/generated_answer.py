def all_left_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for num in range(2, x):
        if all((int(num[:i]) for i in range(1, len(num) + 1))) and all((int(num[:i]) % 2 != 0 for i in range(1, len(num) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)