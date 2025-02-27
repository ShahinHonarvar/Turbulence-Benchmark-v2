def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    primes = [2]
    for i in range(3, x + 1, 2):
        if is_prime(i):
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if not (prime_str[:i] in primes and prime_str[i:] in primes):
                break
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)