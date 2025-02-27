def all_left_truncatable_prime(numbers):
    x = numbers[20]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num) % 10 != 0 and all((int(num[:i]) in primes for i in range(1, len(num)))) for num in str(num))):
            primes.append(num)
    return sorted(primes, reverse=True)