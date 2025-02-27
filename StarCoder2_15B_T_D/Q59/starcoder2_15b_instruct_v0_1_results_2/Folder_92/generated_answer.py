def all_left_truncatable_prime(tup):
    x = tup[7]

    def is_left_truncatable_prime(num):
        if num in [2, 3, 5, 7]:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        while num > 0:
            if num in [2, 3, 5, 7]:
                return True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            num //= 10
        return False
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)])