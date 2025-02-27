def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if len(str_n) == 1 or (is_prime(int(str_n)) and all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i])) for i in range(1, len(str_n))))):
            return True
        return False
    x = numbers[792]
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)])