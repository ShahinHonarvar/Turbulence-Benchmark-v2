def all_left_right_truncatable_prime(tup):
    x = tup[35]

    def is_truncatable_prime(num):
        if num < 2 or (num > 2 and num % 2 == 0):
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        while num >= 10:
            num = int(str(num)[1:])
            if num < 2 or (num > 2 and num % 2 == 0):
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)