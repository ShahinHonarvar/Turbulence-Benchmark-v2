def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = numbers[23] if len(numbers) > 23 else 10 ** 20
    str_x = str(x)
    return [p for p in range(2, x) if all((is_prime(int(str_x[:i])) for i in range(1, len(str_x) + 1)))]