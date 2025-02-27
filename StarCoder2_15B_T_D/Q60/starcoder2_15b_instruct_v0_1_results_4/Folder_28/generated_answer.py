def all_left_right_truncatable_prime(x):
    """
    This function takes a tuple of positive integers as input and returns a list of all left-and-right-truncatable prime numbers less than or equal to the 20th element of the tuple.
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    x = x[19]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)