def all_left_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(int(str(n)[:-1])):
                return False
            n = int(str(n)[:-1])
        return True
    x = input_tuple[38]
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)