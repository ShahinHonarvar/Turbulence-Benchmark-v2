def all_right_truncatable_prime(input_tuple):
    """
    This function takes a tuple of positive integers and returns a sorted list of all right-truncatable prime numbers less than the integer at index 760.
    """
    x = input_tuple[760]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    """
    This function takes an integer and returns True if it is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True