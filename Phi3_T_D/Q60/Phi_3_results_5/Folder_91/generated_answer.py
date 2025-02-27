def all_left_right_truncatable_prime(range_tuple):

    def is_right_truncatable(num, base):
        while num > 0:
            if not is_prime(num):
                return False
            num = num % base // 10
        return True

    def is_left_truncatable(num, base):
        while num > 0:
            if not is_prime(num):
                return False
            num = num // base % base ** 2
        return True

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    lower_bound, upper_bound = range_tuple
    result = [n for n in range(lower_bound, upper_bound + 1) if is_left_truncatable(n, 10) and is_right_truncatable(n, 10)]
    return sorted(result, reverse=True)