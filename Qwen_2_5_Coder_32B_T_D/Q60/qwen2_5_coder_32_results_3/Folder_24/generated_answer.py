def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str) - 1):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return is_prime(n) and is_prime(int(n_str[1:])) and is_prime(int(n_str[:-1]))
    x = t[65]
    result = [i for i in range(11, x + 1) if is_lr_truncatable_prime(i)]
    return sorted(result, reverse=True)