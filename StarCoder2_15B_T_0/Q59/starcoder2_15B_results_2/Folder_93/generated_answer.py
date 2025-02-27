def all_left_truncatable_prime(input_tuple):
    x = input_tuple[11]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)))