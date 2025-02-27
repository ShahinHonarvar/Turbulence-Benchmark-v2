def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]

    def is_lr_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:-i]))):
                return False
        return True
    lr_truncatable_primes = [i for i in range(10, x + 1) if is_prime(i) and is_lr_truncatable_prime(i)]
    return sorted(lr_truncatable_primes, reverse=True)