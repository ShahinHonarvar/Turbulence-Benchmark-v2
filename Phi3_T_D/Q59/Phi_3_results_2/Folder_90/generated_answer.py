def all_left_truncatable_prime(values):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = values[466]

    def is_left_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    left_truncatables = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(left_truncatables, reverse=True)