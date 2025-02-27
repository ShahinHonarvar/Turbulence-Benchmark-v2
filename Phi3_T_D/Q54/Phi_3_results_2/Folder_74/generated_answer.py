def all_right_truncatable_prime(numbers):
    x = numbers[36]
    right_truncatable_primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(prime, x):
        if prime > x:
            return False
        truncated_prime = prime
        while truncated_prime > 0:
            if not is_prime(truncated_prime):
                return False
            truncated_prime //= 10
        return True
    for i in range(10, x):
        if is_prime(i) and is_right_truncatable(i, x):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)[1:]