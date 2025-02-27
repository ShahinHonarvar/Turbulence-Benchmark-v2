def all_right_truncatable_prime(input_tuple):
    """
    This function takes an argument which is a tuple of positive integers.
    Let x be the integer at index 81. The function should return the sorted list
    of all right-truncatable prime numbers less than x. The returned list should
    be sorted in descending order. If there is no such right-truncatable prime number,
    the function should return an empty list. A right-truncatable prime number is a
    prime number that remains prime when the last rightmost digit is successively removed.
    """
    x = input_tuple[81]
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
    This function checks if a given number is a prime number.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True