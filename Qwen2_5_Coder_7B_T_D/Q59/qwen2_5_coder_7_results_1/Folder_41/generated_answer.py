def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num) % 2 != 0 and int(num) % i != 0 for i in range(3, int(int(num) ** 0.5) + 1, 2))):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        if all((int(prime[:i]) in primes for i in range(1, len(prime)))):
            left_truncatable_primes.append(int(prime))
    return sorted(left_truncatable_primes, reverse=True)