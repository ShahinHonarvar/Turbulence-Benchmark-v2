def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(prime_str):
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:-i])):
                return False
        return True
    for prime in primes:
        prime_str = str(prime)
        if is_truncatable(prime_str):
            truncatable_primes.append(prime)
    for i in range(11, x + 1):
        prime_str = str(i)
        if is_prime(i) and is_truncatable(prime_str):
            primes.append(i)
    return truncatable_primes