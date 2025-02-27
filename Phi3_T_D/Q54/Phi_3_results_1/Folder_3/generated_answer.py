def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        truncated = prime_str
        while len(truncated) > 0 and is_prime(int(truncated)):
            truncated = truncated[:-1]
        if not truncated:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)