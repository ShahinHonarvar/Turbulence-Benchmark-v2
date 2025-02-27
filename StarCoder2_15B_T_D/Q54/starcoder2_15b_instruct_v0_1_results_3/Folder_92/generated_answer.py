def all_right_truncatable_prime(args):
    """
    This function takes a tuple of positive integers as an argument.
    It returns a sorted list of all right-truncatable prime numbers
    less than the integer at index 7 of the argument tuple.
    """
    x = args[7]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(1, len(str(i))):
            truncated_number = int(str(i)[:-j])
            if not is_prime(truncated_number):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True