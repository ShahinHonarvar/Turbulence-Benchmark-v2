def all_left_right_truncatable_prime(input_tuple: tuple) -> list:
    """
    Returns a list of all left-and-right-truncatable prime numbers less than or equal to the
    integer at index 14 of the input tuple.
    """
    x = input_tuple[14]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[j + 1:])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            truncated_num = int(str(i)[:-j - 1])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(num: int) -> bool:
    """Returns True if the given number is prime, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True