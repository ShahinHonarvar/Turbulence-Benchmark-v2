def all_right_truncatable_prime(x):

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x[0] - 1, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result