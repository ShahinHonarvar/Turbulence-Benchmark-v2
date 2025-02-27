def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:-j])
            if left_truncation % 2 == 0 or right_truncation % 2 == 0:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes