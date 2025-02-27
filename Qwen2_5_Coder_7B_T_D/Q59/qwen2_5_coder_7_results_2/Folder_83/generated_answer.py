def all_left_truncatable_prime(numbers):
    x = numbers[24]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num) % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime and all((int(str_prime[:i]) in primes for i in range(1, len(str_prime)))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)