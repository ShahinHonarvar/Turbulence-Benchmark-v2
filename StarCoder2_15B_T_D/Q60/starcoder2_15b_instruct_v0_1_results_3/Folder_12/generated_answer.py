def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
    result = []
    for n in sorted(list(x), reverse=True):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    return result