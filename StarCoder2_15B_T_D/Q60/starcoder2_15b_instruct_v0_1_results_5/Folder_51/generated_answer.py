def all_left_right_truncatable_prime(x):
    left_right_truncatable_primes = []
    x = x[0]
    for i in range(2, x + 1):
        is_left_right_truncatable_prime = True
        num_str = str(i)
        if '0' in num_str:
            continue
        for j in range(len(num_str)):
            truncated_num_str = num_str[j:]
            if j > 0:
                truncated_num_str = num_str[:j]
            if int(truncated_num_str) < 2 or not is_prime(int(truncated_num_str)):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True