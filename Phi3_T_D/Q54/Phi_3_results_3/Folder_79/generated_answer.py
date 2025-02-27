def all_right_truncatable_prime(numbers):
    x = numbers[91]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_right(n):
        truncated = []
        while n > 0:
            if is_prime(n):
                truncated.append(n)
            n = n // 10
        return truncated
    right_truncatable_primes = truncate_right(x)
    return sorted(list(set(right_truncatable_primes))) if right_truncatable_primes else []