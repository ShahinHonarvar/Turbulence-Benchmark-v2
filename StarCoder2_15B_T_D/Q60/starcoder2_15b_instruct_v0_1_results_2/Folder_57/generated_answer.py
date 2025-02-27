def all_left_right_truncatable_prime(x):

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        else:
            return is_prime(num) and is_truncatable_prime(int(str(num)[1:])) and is_truncatable_prime(int(str(num)[:-1]))

    def is_prime(num):
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
    x = x[54]
    return sorted([num for num in range(2, x + 1) if is_truncatable_prime(num)], reverse=True)