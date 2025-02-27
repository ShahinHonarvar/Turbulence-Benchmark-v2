def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(prime):
        str_prime = str(prime)
        return all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:i + 1])) for i in range(len(str_prime))))
    x = numbers[29]
    truncatable_primes = []
    for prime in (p for p in range(2, x + 1) if is_prime(p)):
        if is_truncatable(prime):
            truncatable_primes.append(prime)
    return truncatable_primes