def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    primes = set()
    for num in range(2, x + 1):
        if all((int(digit) != 0 and all((int(digit) != 0 for digit in str(num))) for num in range(2, num + 1))):
            primes.add(num)
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if all((int(str_prime[:i]) in primes and int(str_prime[i:]) in primes for i in range(1, len(str_prime)))):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)