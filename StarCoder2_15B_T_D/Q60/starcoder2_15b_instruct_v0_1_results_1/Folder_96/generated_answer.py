def all_left_right_truncatable_prime(t):
    x = t[29]

    def is_truncatable_prime(num):
        num_str = str(num)
        if num < 10:
            return False
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i + 1:])):
                return False
            if not is_prime(int(num_str[:len(num_str) - i - 1])):
                return False
        return is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    truncatable_primes.sort()
    return truncatable_primes