def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)