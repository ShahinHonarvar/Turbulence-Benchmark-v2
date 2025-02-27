def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str) - 1):
            if not is_prime(int(num_str[i:-i])):
                return False
        return is_prime(n)
    x = numbers[89]
    lr_truncatable_primes = [n for n in range(10, x + 1) if is_lr_truncatable_prime(n)]
    return sorted(lr_truncatable_primes, reverse=True)