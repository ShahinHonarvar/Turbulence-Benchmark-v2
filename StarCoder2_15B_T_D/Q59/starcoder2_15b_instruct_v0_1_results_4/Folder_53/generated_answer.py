def all_left_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = tuple_of_positive_integers[86]
    return sorted([n for n in range(x) if is_left_truncatable(n)], reverse=True)