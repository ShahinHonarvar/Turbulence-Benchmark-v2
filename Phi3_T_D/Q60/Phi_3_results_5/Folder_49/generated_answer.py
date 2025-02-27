def all_left_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(p):
        str_p = str(p)
        return all((is_prime(int(str_p[i:])) for i in range(len(str_p)))) and all((is_prime(int(str_p[:-i])) for i in range(1, len(str_p))))
    x = input_tuple[14]
    result = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return result