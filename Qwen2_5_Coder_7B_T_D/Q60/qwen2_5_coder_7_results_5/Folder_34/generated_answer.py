def all_left_right_truncatable_prime(numbers):
    x = numbers[18]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num = n
        while num > 0:
            if not is_prime(num):
                return False
            num = num // 10
        num = n
        while num > 0:
            if not is_prime(num):
                return False
            num = num % (10 ** len(str(num)) - 1)
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)