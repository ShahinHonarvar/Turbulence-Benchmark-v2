def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        s = str(n)
        for i in range(len(s) - 1):
            if not is_prime(int(s[i + 1:])) or not is_prime(int(s[:-(i + 1)])):
                return False
        return True
    x = numbers[79]
    lr_truncatable_primes = [n for n in range(10, x + 1) if '0' not in str(n) and is_prime(n) and is_lr_truncatable_prime(n)]
    return sorted(lr_truncatable_primes, reverse=True)