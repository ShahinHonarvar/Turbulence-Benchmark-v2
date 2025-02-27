def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if int(num_str[i + 1:]) % num != 0 or int(num_str[:i + 1]) % num != 0:
                return False
        return True
    truncatable_primes = []
    for num in range(1, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes