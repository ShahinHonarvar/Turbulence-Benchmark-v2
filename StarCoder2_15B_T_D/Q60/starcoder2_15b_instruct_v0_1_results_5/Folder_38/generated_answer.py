def all_left_right_truncatable_prime(t):
    x = t[28]

    def is_truncatable_prime(num):
        num_str = str(num)
        if num < 10:
            return False
        if num in [2, 3, 5, 7]:
            return True
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if int(num_str[i:]) % 2 == 0 or int(num_str[:i]) % 2 == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes