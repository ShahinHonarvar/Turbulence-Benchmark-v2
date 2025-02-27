def all_right_truncatable_prime(num_tuple):
    x = num_tuple[429]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    right_truncatable_primes = [i for i in range(x - 1, 7, -1) if is_right_truncatable(i)]
    return right_truncatable_primes