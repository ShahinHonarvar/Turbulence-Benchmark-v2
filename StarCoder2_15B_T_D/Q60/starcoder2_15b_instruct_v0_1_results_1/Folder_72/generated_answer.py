def all_left_right_truncatable_prime(x):
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(1, x + 1):
        is_left_truncatable = True
        is_right_truncatable = True
        num_str = str(i)
        for j in range(len(num_str) - 1):
            if int(num_str[j + 1:]) % i != 0:
                is_left_truncatable = False
                break
        for j in range(len(num_str) - 1):
            if int(num_str[:-j - 1]) % i != 0:
                is_right_truncatable = False
                break
        if is_left_truncatable and is_right_truncatable:
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes