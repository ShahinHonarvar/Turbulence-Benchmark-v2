def all_left_right_truncatable_prime(numbers):
    """
    Find all left-and-right-truncatable prime numbers less than or equal to the integer at index 100.
    """
    x = numbers[100]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) not in truncatable_primes or int(str(i)[:j + 1]) not in truncatable_primes:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)