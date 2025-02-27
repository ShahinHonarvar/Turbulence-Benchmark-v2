def all_left_truncatable_prime(t):
    x = t[0]
    prime_list = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    left_truncatable_prime_list = []
    for prime in prime_list:
        is_left_truncatable = True
        truncated_prime = prime
        while truncated_prime > 0:
            truncated_prime //= 10
            if truncated_prime == 0:
                break
            if truncated_prime not in prime_list:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_prime_list.append(prime)
    return sorted(left_truncatable_prime_list)