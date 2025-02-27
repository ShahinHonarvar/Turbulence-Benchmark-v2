def all_right_truncatable_prime(numbers):
    x = numbers[6]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while str_prime:
            if not all((int(str_prime[:i]) % j != 0 for i in range(1, len(str_prime) + 1) for j in range(2, int(int(str_prime[:i]) ** 0.5) + 1))):
                break
            str_prime = str_prime[:-1]
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)