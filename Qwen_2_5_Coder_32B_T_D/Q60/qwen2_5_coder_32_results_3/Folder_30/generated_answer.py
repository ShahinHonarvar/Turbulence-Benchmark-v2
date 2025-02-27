def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n) - 1):
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
                return False
        return is_prime(n)
    x = numbers[37]
    truncatable_primes = [n for n in range(10, x + 1) if is_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)