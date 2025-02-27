def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(num):
        if not is_prime(num):
            return False
        str_num = str(num)
        return is_truncatable_left(str_num, num) and is_truncatable_right(str_num, num)

    def is_truncatable_left(nstr, n):
        while len(nstr) > 0:
            if not is_prime(int(nstr)):
                return False
            nstr = nstr[1:]
        return True

    def is_truncatable_right(nstr, n):
        while len(nstr) > 0:
            if not is_prime(int(nstr)):
                return False
            nstr = nstr[:-1]
        return True
    x = numbers[65]
    truncatables = sorted([num for num in range(2, x + 1) if is_truncatable(num)], reverse=True)
    return truncatables