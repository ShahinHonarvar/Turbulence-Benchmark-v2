def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    if '0' in str(num):
        return False
    num_str = str(num)
    left, right = (num_str[0], num_str[-1])
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[36]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)