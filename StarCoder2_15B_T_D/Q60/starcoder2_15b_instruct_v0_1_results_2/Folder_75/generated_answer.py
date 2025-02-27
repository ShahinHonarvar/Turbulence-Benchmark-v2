def all_left_right_truncatable_prime(x):

    def is_truncatable_prime(num, direction):
        if num < 10:
            return is_prime(num)
        if not is_prime(num):
            return False
        return is_truncatable_prime(int(str(num)[1:]) if direction == 'left' else int(str(num)[:-1]), direction)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = x[41]
    return sorted([num for num in range(2, x + 1) if is_truncatable_prime(num, 'left') and is_truncatable_prime(num, 'right')])