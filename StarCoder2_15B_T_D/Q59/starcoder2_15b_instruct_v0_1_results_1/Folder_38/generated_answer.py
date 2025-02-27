def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[28]

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True
    return sorted((n for n in range(2, x) if is_left_truncatable_prime(n)))