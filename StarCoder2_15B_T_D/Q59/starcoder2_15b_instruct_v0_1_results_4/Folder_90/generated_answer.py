def all_left_truncatable_prime(numbers):
    """
    Returns a list of all left-truncatable prime numbers less than x,
    where x is the 467th element of the input tuple.
    """
    x = numbers[466]
    prime_numbers = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i))):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True