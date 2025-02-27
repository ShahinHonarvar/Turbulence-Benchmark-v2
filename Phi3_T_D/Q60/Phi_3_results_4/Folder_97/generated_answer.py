def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, original):
        if not is_prime(n):
            return False
        str_n = str(n)
        if not all((digit not in {'0', '2', '4', '5', '6', '8'} for digit in str_n)):
            return False
        while len(str_n) > 1:
            n = int(str_n[1:])
            if not is_prime(n):
                return False
            str_n = str(n)
        return True
    x = numbers[645]
    result = [i for i in range(2, x + 1) if is_truncatable_prime(i, x)]
    return result