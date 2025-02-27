def all_right_truncatable_prime(t):
    x = t[30]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generate_truncatable_primes(n):
        if n < 10:
            return [n]
        result = []
        for i in range(10):
            if is_truncatable_prime(n):
                result.extend(generate_truncatable_primes(n // 10))
        return result
    return sorted(generate_truncatable_primes(x))