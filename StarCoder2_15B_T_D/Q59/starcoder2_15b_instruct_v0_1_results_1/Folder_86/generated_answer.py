def all_left_truncatable_prime(input_tuple):
    x = input_tuple[126]

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return not str(n).startswith('0')
    return sorted(filter(is_left_truncatable_prime, range(x)), reverse=True)