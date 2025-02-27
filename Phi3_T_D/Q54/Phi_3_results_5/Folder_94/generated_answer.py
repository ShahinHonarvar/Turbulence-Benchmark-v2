def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, seen):
        if n == 0:
            return True
        if n in seen or not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10, seen + [n])
    primes = [n for n in range(2, numbers[43]) if is_right_truncatable_prime(n, [])]
    return sorted(primes)