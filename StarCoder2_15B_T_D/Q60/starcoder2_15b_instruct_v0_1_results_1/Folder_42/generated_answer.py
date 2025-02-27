def all_left_right_truncatable_prime(tup):
    x = tup[64]
    left_truncatable_primes = [2, 3, 5, 7]
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        num_str = str(i)
        if '0' in num_str:
            continue
        is_left_truncatable = True
        is_right_truncatable = True
        for j in range(1, len(num_str)):
            truncated_num = int(num_str[j:])
            if truncated_num % 2 == 0 or truncated_num % 3 == 0 or truncated_num % 5 == 0 or (truncated_num % 7 == 0):
                is_left_truncatable = False
                break
        for j in range(len(num_str) - 1, 0, -1):
            truncated_num = int(num_str[:j])
            if truncated_num % 2 == 0 or truncated_num % 3 == 0 or truncated_num % 5 == 0 or (truncated_num % 7 == 0):
                is_right_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    result = []
    for prime in left_truncatable_primes:
        if prime in right_truncatable_primes:
            result.append(prime)
    result.sort(reverse=True)
    return result