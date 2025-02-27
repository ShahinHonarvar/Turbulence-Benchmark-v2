def all_right_truncatable_prime(x):
    if type(x) is not tuple or len(x) < 79 or (not all((isinstance(i, int) and i > 0 for i in x))):
        raise ValueError('Invalid input: The argument must be a tuple of positive integers with a length of at least 79.')
    x = x[78]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if truncated_number % 2 == 0 or truncated_number % 3 == 0 or truncated_number % 5 == 0 or (truncated_number % 7 == 0):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)