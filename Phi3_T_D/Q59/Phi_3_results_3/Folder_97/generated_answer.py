def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = num % 10 ** (len(str(num)) - 1)
        return True
    x = t[645]
    return [num for num in range(2, x) if is_left_truncatable(num)]