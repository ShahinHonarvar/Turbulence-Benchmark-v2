def all_left_truncatable_prime(args):
    assert isinstance(args, tuple), 'Invalid input type'
    assert len(args) == 1, 'Invalid input length'
    assert isinstance(args[0], int) and args[0] > 0, 'Invalid input value'
    x = args[0]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        return True
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])