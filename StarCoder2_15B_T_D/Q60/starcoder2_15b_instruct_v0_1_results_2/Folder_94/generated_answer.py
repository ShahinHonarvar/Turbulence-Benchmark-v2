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
        digits = [int(d) for d in str(n)]
        for i in range(len(digits) - 1):
            left_trunc = int(''.join((str(d) for d in digits[i + 1:])))
            right_trunc = int(''.join((str(d) for d in digits[:len(digits) - i - 1])))
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    result = []
    for i in range(11, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)