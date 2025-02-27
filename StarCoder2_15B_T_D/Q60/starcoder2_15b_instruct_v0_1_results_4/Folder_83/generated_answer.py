def all_left_right_truncatable_prime(tup):
    x = tup[24]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
        num_str = num_str[:-1]
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True