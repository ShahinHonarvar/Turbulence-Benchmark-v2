def all_right_truncatable_prime(input_tuple):
    """
    Given a tuple of positive integers, returns a sorted list of all right-truncatable prime
    numbers less than the integer at index 11. If there are no right-truncatable prime numbers,
    returns an empty list.
    """
    x = input_tuple[11]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[j + 1:])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    """Helper function to check if a number is prime."""
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