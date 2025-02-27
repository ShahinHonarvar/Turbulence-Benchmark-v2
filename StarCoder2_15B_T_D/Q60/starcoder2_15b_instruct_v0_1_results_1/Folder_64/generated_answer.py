def all_left_right_truncatable_prime(tup):
    x = tup[4]

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i + 1:])):
                return False
            if not is_prime(int(num_str[:len(num_str) - i - 1])):
                return False
        return is_prime(num)

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)