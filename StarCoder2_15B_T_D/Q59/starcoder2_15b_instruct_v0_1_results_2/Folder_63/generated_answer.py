def all_left_truncatable_prime(numbers):
    x = numbers[88]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(1, len(str(i))):
            if int(str(i)[j:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)