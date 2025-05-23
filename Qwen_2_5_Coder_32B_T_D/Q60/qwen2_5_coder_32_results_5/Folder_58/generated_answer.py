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
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = numbers[975]
    lr_trunc_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num) and is_lr_truncatable_prime(num):
            lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes, reverse=True)