def all_left_right_truncatable_prime(tuple_of_positive_integers):
    """
    Find all left-and-right-truncatable prime numbers less than or equal to x,
    where x is the integer at index 645.
    """
    left_right_truncatable_primes = []
    x = tuple_of_positive_integers[645]
    for i in range(2, x + 1):
        is_left_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_left_right_truncatable_prime = False
                break
            truncated_number = int(str(i)[:len(str(i)) - j])
            if not is_prime(truncated_number):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_prime(number):
    """
    Check if a given number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True