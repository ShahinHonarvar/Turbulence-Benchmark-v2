def all_left_right_truncatable_prime(numbers):
    """
    This function takes a tuple of positive integers, finds the 175th number,
    and then returns a list of all left- and right-truncatable prime numbers
    less than or equal to the 175th number.
    """
    x = numbers[175]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if not is_prime(truncated_number):
                is_truncatable_prime = False
                break
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    """
    This function checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True