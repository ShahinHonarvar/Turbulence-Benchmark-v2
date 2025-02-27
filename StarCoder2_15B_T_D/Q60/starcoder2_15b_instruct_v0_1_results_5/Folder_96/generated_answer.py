def all_left_right_truncatable_prime(tup):
    x = tup[29]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        is_left_right_truncatable = True
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                is_left_right_truncatable = False
                break
            truncated_num = int(num_str[:len(num_str) - i])
            if not is_prime(truncated_num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True