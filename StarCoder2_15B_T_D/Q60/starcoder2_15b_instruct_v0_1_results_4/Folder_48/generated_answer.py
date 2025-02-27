def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if is_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    while len(num_str) >= 2:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True