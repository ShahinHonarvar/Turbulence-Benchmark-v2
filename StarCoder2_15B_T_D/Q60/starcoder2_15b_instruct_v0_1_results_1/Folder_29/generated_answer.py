def all_left_right_truncatable_prime(numbers):
    """
    Find all left-and-right truncatable prime numbers less than or equal to the number at index 55 of the given tuple.
    """
    x = numbers[55]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:-j - 1])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True