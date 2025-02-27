def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)