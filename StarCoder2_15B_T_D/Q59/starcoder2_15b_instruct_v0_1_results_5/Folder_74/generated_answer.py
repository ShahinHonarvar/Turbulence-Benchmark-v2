from math import sqrt

def all_left_truncatable_prime(input_tuple):
    """
    This function returns a list of all left-truncatable prime numbers less than the integer at index 36.
    """
    x = input_tuple[36]
    is_prime = lambda n: all((n % i != 0 for i in range(2, int(sqrt(n)) + 1)))
    left_truncatable_prime = lambda n: all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))
    return sorted((n for n in range(2, x) if left_truncatable_prime(n)))