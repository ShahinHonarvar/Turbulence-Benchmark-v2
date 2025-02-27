def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n)) + 1):
            if not is_prime(int(str(n)[i - 1:])):
                return False
        return True
    limit = x[0]
    primes = [num for num in range(2, limit) if is_prime(num)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes, reverse=True)