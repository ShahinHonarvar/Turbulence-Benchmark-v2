def all_left_truncatable_prime(num_tuple):
    n = num_tuple[433]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = num % 10 ** (len(str(num)) - 1) // 10
        return True
    return sorted([i for i in range(2, n) if is_truncatable(i)], reverse=True)