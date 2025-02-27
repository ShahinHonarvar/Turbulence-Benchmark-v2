def all_left_right_truncatable_prime(numbers):
    """
    This function returns a list of all left-and-right-truncatable prime numbers less
    than or equal to the 803th number in the tuple.
    """
    x = numbers[803]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:j + 1])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True