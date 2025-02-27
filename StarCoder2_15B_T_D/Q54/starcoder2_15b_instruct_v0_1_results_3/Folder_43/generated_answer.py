def is_prime(num):
    """Checks whether a number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_integers):
    """
    Returns the sorted list of all right-truncatable prime numbers
    less than the integer at index 89 in the given tuple.
    """
    x = tuple_of_integers[89]
    right_truncatable_primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)