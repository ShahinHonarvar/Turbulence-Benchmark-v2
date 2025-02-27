def all_left_truncatable_prime(input_tuple):
    x = input_tuple[39]

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0:
            return False
        return is_left_truncatable_prime(num // 10) and is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(x)), reverse=True)