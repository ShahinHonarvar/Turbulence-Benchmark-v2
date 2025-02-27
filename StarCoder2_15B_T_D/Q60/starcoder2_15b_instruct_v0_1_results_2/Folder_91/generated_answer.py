def all_left_right_truncatable_prime(x):
    """
    This function takes a tuple of positive integers as an argument.
    The function returns a list of all left-and-right-truncatable prime numbers
    less than or equal to the first element of the tuple. The list is sorted
    in descending order. If no left-and-right-truncatable prime number exists
    in the specified range, the function returns an empty list.
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    left_right_truncatable_primes = [n for n in range(2, x[0] + 1) if is_prime(n)]
    for n in left_right_truncatable_primes[:]:
        while len(str(n)) > 1:
            n = truncate_left(n)
            if not is_prime(n):
                left_right_truncatable_primes.remove(n)
                break
    for n in left_right_truncatable_primes[:]:
        while len(str(n)) > 1:
            n = truncate_right(n)
            if not is_prime(n):
                left_right_truncatable_primes.remove(n)
                break
    return sorted(left_right_truncatable_primes, reverse=True)