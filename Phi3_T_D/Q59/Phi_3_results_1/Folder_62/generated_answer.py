def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not all((digit != '0' for digit in str(n))):
            return False
        if not is_prime(n):
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    x = numbers[70]
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable(p)]
    return left_truncatable_primes