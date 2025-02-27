def all_left_right_truncatable_prime(numbers):
    x = numbers[85]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if truncated_number % 2 == 0 or truncated_number % 3 == 0:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)