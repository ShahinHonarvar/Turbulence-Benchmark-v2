def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[14]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True