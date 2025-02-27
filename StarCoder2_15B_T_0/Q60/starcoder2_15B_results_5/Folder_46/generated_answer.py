def all_left_right_truncatable_prime(x):
    x = x[0]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return is_prime(num)
    if num_str[0] == '0' or num_str[-1] == '0':
        return False
    return is_left_right_truncatable_prime(int(num_str[1:])) and is_left_right_truncatable_prime(int(num_str[:-1]))