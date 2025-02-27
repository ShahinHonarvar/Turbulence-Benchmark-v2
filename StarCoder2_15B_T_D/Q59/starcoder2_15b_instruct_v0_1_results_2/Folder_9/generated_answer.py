def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[29]

    def is_left_truncatable_prime(num):
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)