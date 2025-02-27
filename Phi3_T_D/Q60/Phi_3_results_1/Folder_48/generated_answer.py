def all_left_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n, truncatable_primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not str_n[i:] in truncatable_primes:
                return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    truncatable_primes = {'2', '3', '5', '7'}
    x = input_tuple[835]
    left_right_truncatable = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i, truncatable_primes):
            left_right_truncatable.append(i)
    return left_right_truncatable