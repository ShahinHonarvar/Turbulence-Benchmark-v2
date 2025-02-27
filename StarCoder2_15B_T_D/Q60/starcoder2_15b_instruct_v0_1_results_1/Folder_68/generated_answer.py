def all_left_right_truncatable_prime(x):
    left_right_truncatable_primes = []
    for i in range(11, x[0] + 1):
        is_left_right_truncatable = True
        num_str = str(i)
        for j in range(len(num_str)):
            left_num = int(num_str[j:])
            right_num = int(num_str[:len(num_str) - j])
            if left_num < 11 or right_num < 11:
                is_left_right_truncatable = False
                break
            if not is_left_right_truncatable_prime(left_num) or not is_left_right_truncatable_prime(right_num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True