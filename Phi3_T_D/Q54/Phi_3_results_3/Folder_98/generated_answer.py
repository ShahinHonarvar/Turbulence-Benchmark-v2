def all_right_truncatable_prime(numbers):
    x = numbers[8]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, i=0):
        if n < x:
            return False
        if not is_prime(n):
            return False
        str_n = str(n)
        if len(str_n) == 1:
            return True
        return is_right_truncatable_prime(int(str_n[:-1]), i + 1)
    right_truncatables = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            right_truncatables.append(i)
    return right_truncatables