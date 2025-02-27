def all_right_truncatable_prime(numbers):
    """
    Returns a sorted list of all right-truncatable prime numbers less than x,
    where x is the integer at index 96 in the given tuple of positive integers.
    The returned list is sorted in descending order.
    """
    x = numbers[96]
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

def is_prime(number):
    """
    Returns True if the given number is prime, False otherwise.
    """
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True