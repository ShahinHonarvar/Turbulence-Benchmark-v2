def all_left_truncatable_prime(input_tuple):
    x = input_tuple[41]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        for digit in str(num):
            if digit == '0':
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes