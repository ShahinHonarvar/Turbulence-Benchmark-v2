def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    if n == 0 or n in primes:
        return False
    return is_prime(n)

def generate_left_truncatable_primes(max_num):
    primes = []
    for num in range(2, max_num):
        if is_prime(num):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        while prime_str and is_left_truncatable_prime(prime_str, {p: True for p in primes} if truncatable_primes else primes):
            truncatable_primes.append(int(prime_str))
            prime_str = prime_str[:-1]
    return sorted(truncatable_primes, reverse=True)

def all_left_truncatable_prime(numbers):
    return generate_left_truncatable_primes(numbers[37])