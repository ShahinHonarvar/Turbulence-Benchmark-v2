def all_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(1, len(str(i))):
            truncated_number = int(str(i)[:-j])
            if truncated_number < 2 or not all((truncated_number % k for k in range(2, int(truncated_number ** 0.5) + 1))):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)