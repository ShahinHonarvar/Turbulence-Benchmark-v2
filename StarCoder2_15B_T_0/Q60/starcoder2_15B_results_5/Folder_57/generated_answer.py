def all_left_right_truncatable_prime(x):
    x = x[0]
    left_right_truncatable_primes = []
    for i in range(10, x + 1):
        is_left_right_truncatable_prime = True
        num_str = str(i)
        for j in range(len(num_str)):
            truncated_num = int(num_str[j:])
            if not is_prime(truncated_num):
                is_left_right_truncatable_prime = False
                break
            truncated_num = int(num_str[:len(num_str) - j])
            if not is_prime(truncated_num):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True